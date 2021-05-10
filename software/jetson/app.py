#!/usr/bin/env python3

from fastmot.utils import ConfigDecoder, ObjectCenter, Profiler
from utils.parsers import parse_args
from pathlib import Path

import argparse, cv2, fastmot, json

IS_ARDUCAM = False

WITH_GSTREAMER = True

if IS_ARDUCAM:
    from utils import ArducamUtils

def main():
    args = parse_args()

    # Set up logging.
    logging.basicConfig(format='%(asctime)s [%(levelname)8s] %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    logger = logging.getLogger(fastmot.__name__)
    logger.setLevel(logging.DEBUG if args.verbose else logging.INFO)

    # Load config file.
    with open(args.config) as cfg_file:
        config = json.load(cfg_file, cls=ConfigDecoder)

    mot = None
    log = None

    stream = fastmot.VideoIO(config['resize_to'], config['video_io'], args.input_uri, args.output_uri, flip_vertically=args.flip_vertically, flip_horizontally=args.flip_horizontally)

    if args.mot:
        object_x = None
        object_y = None
        center_x = None
        center_y = None
        draw = args.gui or args.output_uri is not None
        obj = ObjectCenter(args)
        mot = fastmot.MOT(config['resize_to'], 
                          stream.cap_dt, 
                          config['mot'], 
                          obj=obj, 
                          draw=draw, 
                          verbose=args.verbose, 
                          sot=not args.no_filter_object_category)

        if args.log is not None:
            Path(args.log).parent.mkdir(parents=True, exist_ok=True)
            log = open(args.log, 'w')

    if args.gui:
        cv2.namedWindow('uARM', cv2.WINDOW_AUTOSIZE)

    if IS_ARDUCAM:
        arducam_utils = ArducamUtils(0)

    logger.info('Starting video capture...')

    stream.start_capture()

    try:
        with Profiler('app') as prof:
            while not args.gui or cv2.getWindowProperty('uARM', 0) >= 0:
                frame = stream.read()

                if frame is None:
                    break

                if IS_ARDUCAM:
                    frame = arducam_utils.convert(frame)

                    if WITH_GSTREAMER:
                        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2YUV_I420)

                    else:
                        frame = resize(frame, 1280.0)

                if args.mot:
                    mot.step(frame, 
                             object_x=object_x, 
                             object_y=object_y, 
                             center_x=center_x, 
                             center_y=center_y)

                    if log is not None:
                        for track in mot.visible_tracks:
                            tl = track.tlbr[:2] / config['resize_to'] * stream.resolution
                            br = track.tlbr[2:] / config['resize_to'] * stream.resolution
                            w, h = br - tl + 1
                            log.write(f'{mot.frame_count},{track.trk_id},{tl[0]:.6f},{tl[1]:.6f},{w:.6f},{h:.6f},-1,-1,-1\n')

                if args.gui:
                    cv2.imshow('uARM', frame)

                    if cv2.waitKey(1) & 0xFF == 27:
                        break

                if args.output_uri is not None:
                    stream.write(frame)

    finally:
        # Clean up resources.
        if log is not None:
            log.close()

        stream.release()
        cv2.destroyAllWindows()

    if args.mot:
        # Timing statistics.
        avg_fps = round(mot.frame_count / prof.duration)
        logger.info('Average FPS: %d', avg_fps)
        mot.print_timing_info()

if __name__ == '__main__':
    main()

