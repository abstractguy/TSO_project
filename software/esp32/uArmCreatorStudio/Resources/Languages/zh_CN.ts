<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE TS>
<TS version="2.1" language="zh_CN" sourcelanguage="en_US">
<context>
    <name>CWPage1</name>
    <message>
        <location filename="../../CalibrationsGUI.py" line="380"/>
        <source>The algorithms in this software will only work if the
</source>
        <translation>若想使用视觉功能，</translation>
    </message>
    <message>
        <location filename="../../CalibrationsGUI.py" line="381"/>
        <source>camera is placed above the robot, and doesn&apos;t move. 

</source>
        <translation>请将摄像头固定在机械臂正上方。

</translation>
    </message>
    <message>
        <location filename="../../CalibrationsGUI.py" line="382"/>
        <source>Please find a way to mount your webcam above the robot,
</source>
        <translation>请想办法将摄像头固定在机械臂正上方，
</translation>
    </message>
    <message>
        <location filename="../../CalibrationsGUI.py" line="383"/>
        <source>in such a way that it has a wide field of view of the
</source>
        <translation>并保证摄像头的视野</translation>
    </message>
    <message>
        <location filename="../../CalibrationsGUI.py" line="384"/>
        <source>robots workspace.
</source>
        <translation>足以涵盖机械臂工作区域。
</translation>
    </message>
    <message>
        <location filename="../../CalibrationsGUI.py" line="387"/>
        <source>Welcome Coordinate Calibration Wizard!
</source>
        <translation>欢迎使用视觉校正向导！
</translation>
    </message>
    <message>
        <location filename="../../CalibrationsGUI.py" line="386"/>
        <source>This will walk you through teaching the camera the position of the robot.</source>
        <translation type="obsolete">请根据引导完成以下步骤，以使摄像头和机械臂记住对方的位置。</translation>
    </message>
    <message>
        <location filename="../../CalibrationsGUI.py" line="389"/>
        <source>

Step 1: Setup</source>
        <translation>

第1步：安装</translation>
    </message>
    <message>
        <location filename="../../CalibrationsGUI.py" line="388"/>
        <source>This will walk you through teaching UCS the position of the robot.</source>
        <translation>请根据向导指引完成校正，让机械臂和摄像头了解彼此的位置。</translation>
    </message>
</context>
<context>
    <name>CWPage2</name>
    <message>
        <location filename="../../CalibrationsGUI.py" line="453"/>
        <source>

Step 2: Robot Placement</source>
        <translation>

第2步：调整uArm姿势</translation>
    </message>
    <message>
        <location filename="../../CalibrationsGUI.py" line="455"/>
        <source>Could not find example gif</source>
        <translation>找不到示例 gif</translation>
    </message>
    <message>
        <location filename="../../CalibrationsGUI.py" line="493"/>
        <source>Getting Height of Ground</source>
        <translation>正在获取离地面的高度</translation>
    </message>
    <message>
        <location filename="../../CalibrationsGUI.py" line="494"/>
        <source>Yes, the end effector is touching the ground</source>
        <translation>是的，末端吸盘已经触碰到桌面/地面</translation>
    </message>
    <message>
        <location filename="../../CalibrationsGUI.py" line="494"/>
        <source>Important!
Before continuing, make sure the robots end effector is touching the ground, </source>
        <translation type="obsolete">重要提示：
在继续下一步之前，请确保uArm末端已经触碰到桌面/地面， </translation>
    </message>
    <message>
        <location filename="../../CalibrationsGUI.py" line="494"/>
        <source>and that it is centered below the camera. The program will read the robots coordinates.

</source>
        <translation type="obsolete">并且uArm位于摄像头正下方。程序会读取uArm坐标。
</translation>
    </message>
    <message>
        <location filename="../../CalibrationsGUI.py" line="440"/>
        <source>Mount the robot to the ground so that it doesn&apos;t move

                 around, to avoid doing this calibration every time the 

                 robot is moved.


                 Without moving the robots base, lower the head of the robot 

                 until the suction cup is barely touching the ground, as shown

                 on the video to the right.


                 Make sure the top of the robots head is still near the 

                 center of the cameras view, and the sucker is touching the

                 ground.</source>
        <translation type="obsolete">校正前请固定uArm。
若在校正过程中，以及校正后移动了uArm，你需要重新做一次校正。

请按照右边的GIF指引，在保证uArm底座固定的情况下，让uArm末端吸盘触碰到桌面/地面（uArm底部所在的平面）。

请确保uArm吸盘在摄像头视野的中心，且吸盘已经触碰到地面。</translation>
    </message>
    <message>
        <location filename="../../CalibrationsGUI.py" line="442"/>
        <source>Mount the robot to the ground so that it doesn&apos;t move

                            around, to avoid doing this calibration every time the 

                            robot is moved.


                            Without moving the robots base, lower the head of the robot 

                            until the suction cup is barely touching the ground, as shown

                            on the video to the right.


                            Make sure the top of the robots head is still near the 

                            center of the cameras view, and the sucker is touching the

                            ground.</source>
        <translation>1. 将uArm固定在平面上。若校正期间或校正后，uArm被移动，则需要重新校正。
2. 如右侧指引所示，让末端吸盘接触uArm底座所在平面。
3. 继续下一步前，请确保机械臂末端处于摄像头视野中心区，且末端吸头已接触平面。</translation>
    </message>
    <message>
        <location filename="../../CalibrationsGUI.py" line="496"/>
        <source>Important!
Before continuing, make sure the robots end effector is touching the ground, and that it is centered below the camera. The program will read the robots coordinates.

</source>
        <translation>重要提示：
请确保末端吸头已触碰uArm所在桌面/地面，且机械臂末端处于摄像头视野中央。
程序将读取uArm坐标位置。</translation>
    </message>
</context>
<context>
    <name>CWPage3</name>
    <message>
        <location filename="../../CalibrationsGUI.py" line="532"/>
        <source>

Step 3: Make a Robot Marker</source>
        <translation>

第3步：添加一个Robot Marker
（使摄像头识别uArm位置）</translation>
    </message>
    <message>
        <location filename="../../CalibrationsGUI.py" line="521"/>
        <source>In order to track the robot, there must be a marker of some

                 sort on the robot. If you have a QR code or detailed 

                 sticker, then place it on the robots head.


                 If you do not have anything readily avaliable, get a piece 

                 of tape- make sure it&apos;s not reflective (non plastic tape is

                 best), draw on it (as show on the right), and place it on

                 the robots head.


                 There must be a lot of detail on the marker in order to

                 track properly. If you finish this tutorial and tracking is

                 not sufficient, then draw on the marker to add more detail.</source>
        <translation>为了让摄像头识别uArm位置，请在uArm末端上方贴上一个标记，我们叫它“Robot Marker”。

要求：
1. 有丰富的细节特征。（如：二维码，图案复杂的贴纸，等等。）
    为保证识别效果，Robot Marker必须有大量的细节特征可供识别。
    若细节特征不够丰富，系统会提醒你重新换一个Robot Marker。
     
2. 不反光。

手边没有现成的素材可以做成Robot Marker？
马上拿起纸笔，发挥你的想象力，画一个能展示你风格的独特Marker吧！</translation>
    </message>
</context>
<context>
    <name>CWPage4</name>
    <message>
        <location filename="../../CalibrationsGUI.py" line="599"/>
        <source>Step 4: Selecting the Marker</source>
        <translation>第4步：选取Robot Marker</translation>
    </message>
    <message>
        <location filename="../../CalibrationsGUI.py" line="672"/>
        <source>You must select an object with more detail.</source>
        <translation>请选取一个细节特征更丰富的识别对象。</translation>
    </message>
    <message>
        <location filename="../../CalibrationsGUI.py" line="677"/>
        <source>Your selected marker does not have enough detail. Only </source>
        <translation>你选取的Robot Marker没有足够多的细节特征。只检测到 </translation>
    </message>
    <message>
        <location filename="../../CalibrationsGUI.py" line="677"/>
        <source> points were found.
Add detail to your marker and try again.</source>
        <translation> 特征点。
请在你的Robot Marker上添加更多细节后再试一次。</translation>
    </message>
    <message>
        <location filename="../../CalibrationsGUI.py" line="692"/>
        <source>Your selected marker is not very detailed, or is too small, only </source>
        <translation>你选取的Robot Marker比较小，或细节特征不是非常丰富， 
</translation>
    </message>
    <message>
        <location filename="../../CalibrationsGUI.py" line="692"/>
        <source> points were found.
</source>
        <translation> 只检测到 个特征点。</translation>
    </message>
    <message>
        <location filename="../../CalibrationsGUI.py" line="692"/>
        <source>Tracking may not be very accurate.</source>
        <translation>追踪效果可能不会非常准确。</translation>
    </message>
    <message>
        <location filename="../../CalibrationsGUI.py" line="696"/>
        <source>Found </source>
        <translation>发现 </translation>
    </message>
    <message>
        <location filename="../../CalibrationsGUI.py" line="696"/>
        <source> Points</source>
        <translation> 特征点</translation>
    </message>
    <message>
        <location filename="../../CalibrationsGUI.py" line="590"/>
        <source>Make sure the robot&apos;s head is in the center of the camera view. Then, click the mouse on the top
                 
right corner of the marker, and drag it to the bottom right corner of the marker.


                 The camera will begin tracking the marker. Try to have more than 500 points on the marker. Move

                 the robot around and make sure that the object can be recognized for the majority of the cameras

                 view.
</source>
        <translation type="obsolete">请确保uArm末端处于摄像头视野的中心，然后用鼠标拖拽选取Robot Marker，摄像头即开始识别Robot Marker。
尽量保证摄像头能检测到至少500个特征点。
移动uArm末端以确保摄像头能持续跟踪Robot Marker的位置。</translation>
    </message>
    <message>
        <location filename="../../CalibrationsGUI.py" line="593"/>
        <source>Make sure the robot&apos;s head is in the center of the camera view. Then, click the mouse on
                 the top 
right corner of the marker, and drag it to the bottom right corner of the marker.


                 The camera will begin tracking the marker. Try to have more than 500 points on the marker. Move

                 the robot around and make sure that the object can be recognized for the majority of the cameras

                 view.
</source>
        <translation>请确保机械臂末端在摄像头视野范围中央。
用鼠标拖动选取你的Robot Marker，摄像头将开始记录它的位置。
选取后，可试着拖动机械臂，确保摄像头能实时追踪Robot Marker的位置。</translation>
    </message>
</context>
<context>
    <name>CWPage5</name>
    <message>
        <location filename="../../CalibrationsGUI.py" line="723"/>
        <source>Start Calibration</source>
        <translation>开始校正</translation>
    </message>
    <message>
        <location filename="../../CalibrationsGUI.py" line="747"/>
        <source>

Final Step:</source>
        <translation>

最后一步：</translation>
    </message>
    <message>
        <location filename="../../CalibrationsGUI.py" line="865"/>
        <source>The marker was not recognized in enough points- it was only seen </source>
        <translation>无法有效识别Robot Marker。 </translation>
    </message>
    <message>
        <location filename="../../CalibrationsGUI.py" line="865"/>
        <source>
	  It must be seen at least </source>
        <translation>
  至少要检测到500个特征点</translation>
    </message>
    <message>
        <location filename="../../CalibrationsGUI.py" line="885"/>
        <source>Calibration did not complete successfully. The following errors occured:
</source>
        <translation>校正失败，错误信息如下：
</translation>
    </message>
    <message>
        <location filename="../../CalibrationsGUI.py" line="889"/>
        <source>Try Again</source>
        <translation>重试</translation>
    </message>
    <message>
        <location filename="../../CalibrationsGUI.py" line="891"/>
        <source>Calibration was successful, </source>
        <translation>校正成功，</translation>
    </message>
    <message>
        <location filename="../../CalibrationsGUI.py" line="920"/>
        <source>    Progress Report: The robot marker has failed to be recognized </source>
        <translation>   进度报告： 摄像头没有识别到Robot Marker。</translation>
    </message>
    <message>
        <location filename="../../CalibrationsGUI.py" line="923"/>
        <source>    Progress Report: The calibration is going well.
</source>
        <translation>   进度报告：校正进度正常。
</translation>
    </message>
    <message>
        <location filename="../../CalibrationsGUI.py" line="926"/>
        <source>    Testing Point:	</source>
        <translation>    检测点： </translation>
    </message>
    <message>
        <location filename="../../CalibrationsGUI.py" line="927"/>
        <source>    Valid Points: 	</source>
        <translation>   有效点： </translation>
    </message>
    <message>
        <location filename="../../CalibrationsGUI.py" line="961"/>
        <source>Robot was disconnected during calibration</source>
        <translation>uArm在校正过程中被断开连接</translation>
    </message>
    <message>
        <location filename="../../CalibrationsGUI.py" line="734"/>
        <source>When you press the Start Calibration button, the robot will go through a set of predefined moves

                        and record the information that it needs.
                        Before beginning:



                        1) Make sure that the robot&apos;s head is more or less centered under the cameras view, and the

                            Robot Marker is being tracked.

                        2) Make sure there is ample space for the robot to move around.

                        3) Make sure the robot is immobile, and mounted to the ground. If you move the robot,

                            you will have to re-run this calibration.
</source>
        <translation type="obsolete">当你点击“开始校正”按钮后，uArm会自动完成一套校正动作。

校正前，请确保：
1）uArm末端在摄像头视野的中心，且摄像头能持续追踪Robot Marker的位置。
2）uArm有足够的活动空间。
3）uArm底座被固定在平面上。若移动uArm位置，则须重新校正一次才能正常使用视觉功能。</translation>
    </message>
    <message>
        <location filename="../../CalibrationsGUI.py" line="859"/>
        <source>The robot marker was never seen! Try restarting the calibration and creating the
                        
	  marker again, making sure that the robot&apos;s head is in view of the camera.
                        

	  Also make sure that the area in the camera view is clear, blank, without too much
                        
	  detail around it- try having a clear workspace with white paper as a background.</source>
        <translation>很抱歉，摄像头没有检测到Robot Marker。
请试着重来一次校正，或更换/加工你的Robot Marker使其细节特征更丰富。

请确保：
1）uArm末端在摄像头视野的中心；
2）背景干净，无过多杂物。可选择用不反光的白纸/白板作为背景。</translation>
    </message>
    <message>
        <location filename="../../CalibrationsGUI.py" line="861"/>
        <source>

	  Try making sure that the robot&apos;s head is centered in the middle of the cameras
                          
	  view in the previous step, and try placing the camera in a higher location.
                          

	  Also make sure that the area around the camera view is clear, blank, without too
                          
	  much detail around it- try having a clear workspace with white paper as a background.</source>
        <translation type="obsolete">小提示：
1）请确保uArm末端在摄像头视野的中心；
2）可试着将摄像头架在更高的位置，以获得更广的视野。
2）请确保背景干净，无过多杂物。可选择用不反光的白纸/白板作为背景。</translation>
    </message>
    <message>
        <location filename="../../CalibrationsGUI.py" line="889"/>
        <source> points were found.
Results will be saved when you click Apply
                        on the calibrations page. Feel free to try this again.

                        Make sure to repeat this calibration whenever you move your camera or move your robot.</source>
        <translation type="obsolete">检测到 个特征点。
若摄像头能持续追踪Robot Marker，请点击“应用”保存检测结果！

如果你在完成校正后移动了摄像头或uArm的位置，请重新校正一次，以正常使用相应的视觉功能。</translation>
    </message>
    <message>
        <location filename="../../CalibrationsGUI.py" line="738"/>
        <source>When you press the Start Calibration button, the robot will go through a set of predefined
                        moves
 and record the information that it needs.
                        Before beginning:



                        1) Make sure that the robot&apos;s head is more or less centered under the cameras view, and the

                            Robot Marker is being tracked.

                        2) Make sure there is ample space for the robot to move around.

                        3) Make sure the robot is immobile, and mounted to the ground. If you move the robot,

                            you will have to re-run this calibration.
</source>
        <translation>继续下一步前，请确保：
1. uArm末端在摄像头视野范围中央，且摄像头能实时追踪Robot Marker的位置。
2. uArm有足够的活动空间。
3. uArm和摄像头位置固定。

点击“开始校正”后，uArm会自动完成校正动作。</translation>
    </message>
    <message>
        <location filename="../../CalibrationsGUI.py" line="865"/>
        <source>

	  Try making sure that the robot&apos;s head is centered in the middle of the cameras
                       
	  view in the previous step, and try placing the camera in a higher location.
                       

	  Also make sure that the area around the camera view is clear, blank, without too
                       
	  much detail around it- try having a clear workspace with white paper as a background.</source>
        <translation>请确保：
1. uArm末端在摄像头视野中央。
    若视线范围不够大，可将摄像头固定在更高的地方。
2. 摄像头视线范围内无杂物。</translation>
    </message>
    <message>
        <location filename="../../CalibrationsGUI.py" line="892"/>
        <source> points were found.
Results will be saved when you click Apply
                       on the calibrations page. Feel free to try this again.

                       Make sure to repeat this calibration whenever you move your camera or move your robot.</source>
        <translation> 特征点被记录
点击“应用”，校正完成。

若此后移动了uArm或摄像头的位置，则需要重新校正。
</translation>
    </message>
</context>
<context>
    <name>CalibrateWindow</name>
    <message>
        <location filename="../../CalibrationsGUI.py" line="59"/>
        <source>A camera must be connected to run this calibration.</source>
        <translation>请接入摄像头。</translation>
    </message>
    <message>
        <location filename="../../CalibrationsGUI.py" line="60"/>
        <source>A robot must be connected to run this calibration.</source>
        <translation>请接入uArm。</translation>
    </message>
    <message>
        <location filename="../../CalibrationsGUI.py" line="62"/>
        <source>Instructions</source>
        <translation>指南</translation>
    </message>
    <message>
        <location filename="../../CalibrationsGUI.py" line="67"/>
        <source>No information for this calibration</source>
        <translation>暂无校正记录</translation>
    </message>
    <message>
        <location filename="../../CalibrationsGUI.py" line="84"/>
        <source>Calibrate Motion Detection</source>
        <translation>动作检测校正</translation>
    </message>
    <message>
        <location filename="../../CalibrationsGUI.py" line="85"/>
        <source>Calibrate Camera/Robot Position</source>
        <translation>“摄像头－uArm”相对位置校正</translation>
    </message>
    <message>
        <location filename="../../CalibrationsGUI.py" line="86"/>
        <source>Cancel</source>
        <translation>取消</translation>
    </message>
    <message>
        <location filename="../../CalibrationsGUI.py" line="87"/>
        <source>Apply</source>
        <translation>应用</translation>
    </message>
    <message>
        <location filename="../../CalibrationsGUI.py" line="158"/>
        <source>Calibrations</source>
        <translation>校正（视觉功能）</translation>
    </message>
    <message>
        <location filename="../../CalibrationsGUI.py" line="166"/>
        <source> Stationary Movement: </source>
        <translation> 静止轨迹： </translation>
    </message>
    <message>
        <location filename="../../CalibrationsGUI.py" line="166"/>
        <source>     Active Movement: </source>
        <translation>      运动轨迹： </translation>
    </message>
    <message>
        <location filename="../../CalibrationsGUI.py" line="171"/>
        <source>Calibration has been run before. </source>
        <translation>你已经校正过了 :) </translation>
    </message>
    <message>
        <location filename="../../CalibrationsGUI.py" line="171"/>
        <source> points of data were collected.</source>
        <translation>已收集 数据。</translation>
    </message>
    <message>
        <location filename="../../CalibrationsGUI.py" line="176"/>
        <source>Step </source>
        <translation>步骤 </translation>
    </message>
    <message>
        <location filename="../../CalibrationsGUI.py" line="197"/>
        <source>Do not make any movement in the cameras view until the next message appears.</source>
        <translation>在下一条提示出现前，请不要在摄像头可视范围内移动机械臂。</translation>
    </message>
    <message>
        <location filename="../../CalibrationsGUI.py" line="270"/>
        <source>Skip to Calibration?</source>
        <translation>直接开始校正？</translation>
    </message>
    <message>
        <location filename="../../CalibrationsGUI.py" line="271"/>
        <source>I want to set a new Robot Marker</source>
        <translation>我想新建一个Robot Marker</translation>
    </message>
    <message>
        <location filename="../../CalibrationsGUI.py" line="273"/>
        <source>Skip to Automatic Calibration</source>
        <translation>直接跳到“自动校正”</translation>
    </message>
    <message>
        <location filename="../../CalibrationsGUI.py" line="275"/>
        <source>It appears this is not the first time you have run this tutorial.

</source>
        <translation>你之前已使用过此教程。

</translation>
    </message>
    <message>
        <location filename="../../CalibrationsGUI.py" line="275"/>
        <source>Would you like to start from scratch, or skip to the automated calibration?

</source>
        <translation>你是否要从头开始，或者直接跳到自动校正？

</translation>
    </message>
    <message>
        <location filename="../../CalibrationsGUI.py" line="275"/>
        <source>(Automated calibration only works if the robot has the same marker on the top</source>
        <translation>（若你在上次校正后更换了机械臂标记，则无法使用自动校正，</translation>
    </message>
    <message>
        <location filename="../../CalibrationsGUI.py" line="275"/>
        <source> of its head as it did when you first ran this calibration.)
</source>
        <translation>请重新校正一次）</translation>
    </message>
</context>
<context>
    <name>CommandList</name>
    <message>
        <location filename="../../ControlPanelGUI.py" line="793"/>
        <source>Ayyy</source>
        <translation></translation>
    </message>
    <message>
        <location filename="../../ControlPanelGUI.py" line="794"/>
        <source>Menu</source>
        <translation>菜单</translation>
    </message>
</context>
<context>
    <name>CommandMenuWidget</name>
    <message>
        <location filename="../../CommandsGUI.py" line="135"/>
        <source>Basic</source>
        <translation>基本功能</translation>
    </message>
    <message>
        <location filename="../../CommandsGUI.py" line="136"/>
        <source>Vision</source>
        <translation>视觉</translation>
    </message>
    <message>
        <location filename="../../CommandsGUI.py" line="137"/>
        <source>Logic</source>
        <translation>逻辑</translation>
    </message>
    <message>
        <location filename="../../CommandsGUI.py" line="138"/>
        <source>Functions</source>
        <translation>自定义</translation>
    </message>
</context>
<context>
    <name>CommandsGUI</name>
    <message>
        <location filename="../../CommandsGUI.py" line="323"/>
        <source>Apply</source>
        <translation>应用</translation>
    </message>
    <message>
        <location filename="../../CommandsGUI.py" line="324"/>
        <source>Cancel</source>
        <translation>取消</translation>
    </message>
    <message>
        <location filename="../../CommandsGUI.py" line="325"/>
        <source>User Manual</source>
        <translation>用户指南</translation>
    </message>
    <message>
        <location filename="../../CommandsGUI.py" line="341"/>
        <source>Parameters</source>
        <translation>参数</translation>
    </message>
    <message>
        <location filename="../../CommandsGUI.py" line="508"/>
        <source>You have not created any trackable objects yet.</source>
        <translation>你还没有创建任何可识别物体。</translation>
    </message>
    <message>
        <location filename="../../CommandsGUI.py" line="509"/>
        <source> Try adding new objects in the Resource Manager!</source>
        <translation>试着新建一个可识别物体吧！</translation>
    </message>
    <message>
        <location filename="../../CommandsGUI.py" line="512"/>
        <source>It looks like you&apos;ve only created one object.</source>
        <translation>你只添加过一个可识别物体。</translation>
    </message>
    <message>
        <location filename="../../CommandsGUI.py" line="513"/>
        <source> Feel free to add new objects in the Resource Manager!</source>
        <translation>
欢迎添加新的可识别物体！</translation>
    </message>
    <message>
        <location filename="../../CommandsGUI.py" line="523"/>
        <source>You have not created any Movement Recordings yet. </source>
        <translation>你还没有录制过运动轨迹。 </translation>
    </message>
    <message>
        <location filename="../../CommandsGUI.py" line="524"/>
        <source>Try creating new recordings in the Resource Manager!</source>
        <translation>试着给uArm录制一段新动作吧！</translation>
    </message>
    <message>
        <location filename="../../CommandsGUI.py" line="529"/>
        <source>You have not created any Functions yet. </source>
        <translation>你还没有创建任何函数/自定义功能。 </translation>
    </message>
    <message>
        <location filename="../../CommandsGUI.py" line="530"/>
        <source>Try creating new functions in the Resource Manager!</source>
        <translation>试着添加新的函数/自定义功能吧！</translation>
    </message>
    <message>
        <location filename="../../CommandsGUI.py" line="606"/>
        <source>Move XYZ</source>
        <translation>移动到 (X,Y,Z)</translation>
    </message>
    <message>
        <location filename="../../CommandsGUI.py" line="607"/>
        <source>Set the robots position.
</source>
        <translation>设置机械臂的位置。
</translation>
    </message>
    <message>
        <location filename="../../CommandsGUI.py" line="608"/>
        <source>If you do not want to set one of the robots axis, simply leave it empty. For example, put y and z 
</source>
        <translation>你可以只填写需要变动的坐标。例如，当你不填写 y 和 z值 </translation>
    </message>
    <message>
        <location filename="../../CommandsGUI.py" line="610"/>
        <source>empty and x to 5 will set the robots x position to 5 while keeping the current Y and Z the same.</source>
        <translation>并设 x 为 5，机械臂的 x 坐标即变为 5 且 y 和 z位置不便。</translation>
    </message>
    <message>
        <location filename="../../CommandsGUI.py" line="635"/>
        <source>Get Position</source>
        <translation>获取坐标</translation>
    </message>
    <message>
        <location filename="../../CommandsGUI.py" line="715"/>
        <source>Relative </source>
        <translation>相对位置/角度（以现有位置/角度为起点）</translation>
    </message>
    <message>
        <location filename="../../CommandsGUI.py" line="737"/>
        <source>   Relative</source>
        <translation>   相对</translation>
    </message>
    <message>
        <location filename="../../CommandsGUI.py" line="691"/>
        <source>Set Wrist Angle</source>
        <translation>设置末端角度</translation>
    </message>
    <message>
        <location filename="../../CommandsGUI.py" line="692"/>
        <source>This command sets the angle of the robots 4th axis, the wrist.</source>
        <translation>这个命令设置机械臂末端（吸盘）的角度。</translation>
    </message>
    <message>
        <location filename="../../CommandsGUI.py" line="709"/>
        <source>Get Angle</source>
        <translation>获取吸盘角度</translation>
    </message>
    <message>
        <location filename="../../CommandsGUI.py" line="1226"/>
        <source>Angle </source>
        <translation>吸盘角度 </translation>
    </message>
    <message>
        <location filename="../../CommandsGUI.py" line="735"/>
        <source>Set the wrist position to </source>
        <translation>将吸盘角度设置为</translation>
    </message>
    <message>
        <location filename="../../CommandsGUI.py" line="735"/>
        <source> degrees</source>
        <translation>度</translation>
    </message>
    <message>
        <location filename="../../CommandsGUI.py" line="746"/>
        <source>Play Movement Recording</source>
        <translation>播放已录制的动作</translation>
    </message>
    <message>
        <location filename="../../CommandsGUI.py" line="766"/>
        <source>Choose a Recording </source>
        <translation>选择一个已录制动作 </translation>
    </message>
    <message>
        <location filename="../../CommandsGUI.py" line="775"/>
        <source>Playback Speed </source>
        <translation>播放速度 </translation>
    </message>
    <message>
        <location filename="../../CommandsGUI.py" line="782"/>
        <source>Play in reverse?</source>
        <translation>倒序播放？</translation>
    </message>
    <message>
        <location filename="../../CommandsGUI.py" line="800"/>
        <source>Play movement recording </source>
        <translation>播放已录制的动作 </translation>
    </message>
    <message>
        <location filename="../../CommandsGUI.py" line="811"/>
        <source>Set Speed</source>
        <translation>设置速度</translation>
    </message>
    <message>
        <location filename="../../CommandsGUI.py" line="828"/>
        <source>Speed (cm/s) </source>
        <translation>速度 (cm/s) </translation>
    </message>
    <message>
        <location filename="../../CommandsGUI.py" line="855"/>
        <source>Detach Servos</source>
        <translation>解锁电机</translation>
    </message>
    <message>
        <location filename="../../CommandsGUI.py" line="856"/>
        <source>Disengage the specified servos on the robot</source>
        <translation>解锁后，你可手动拖拽该电机控制的uArm关节</translation>
    </message>
    <message>
        <location filename="../../CommandsGUI.py" line="940"/>
        <source>Base Servo </source>
        <translation>底座电机 </translation>
    </message>
    <message>
        <location filename="../../CommandsGUI.py" line="941"/>
        <source>Stretch Servo </source>
        <translation>后臂电机</translation>
    </message>
    <message>
        <location filename="../../CommandsGUI.py" line="942"/>
        <source>Height Servo </source>
        <translation>前臂电机</translation>
    </message>
    <message>
        <location filename="../../CommandsGUI.py" line="943"/>
        <source>Wrist Servo </source>
        <translation>末端电机</translation>
    </message>
    <message>
        <location filename="../../CommandsGUI.py" line="970"/>
        <source>  Base</source>
        <translation>  底部</translation>
    </message>
    <message>
        <location filename="../../CommandsGUI.py" line="971"/>
        <source>  Stretch</source>
        <translation>  前后</translation>
    </message>
    <message>
        <location filename="../../CommandsGUI.py" line="972"/>
        <source>  Height</source>
        <translation>  高低</translation>
    </message>
    <message>
        <location filename="../../CommandsGUI.py" line="973"/>
        <source>  Wrist</source>
        <translation>  吸盘</translation>
    </message>
    <message>
        <location filename="../../CommandsGUI.py" line="920"/>
        <source>Attach Servos</source>
        <translation>锁定电机</translation>
    </message>
    <message>
        <location filename="../../CommandsGUI.py" line="921"/>
        <source>Re-engage servos on the robot. This will &apos;stiffen&apos; the servos, and they will resist movement.</source>
        <translation>锁定机械臂的电机，锁定后，你将不能手动拖拽机械臂。</translation>
    </message>
    <message>
        <location filename="../../CommandsGUI.py" line="969"/>
        <source>Servos</source>
        <translation>电机</translation>
    </message>
    <message>
        <location filename="../../CommandsGUI.py" line="984"/>
        <source>Activate Gripper</source>
        <translation>开启吸盘/夹子</translation>
    </message>
    <message>
        <location filename="../../CommandsGUI.py" line="985"/>
        <source>Activates the robots gripper</source>
        <translation>开始吸取/夹取</translation>
    </message>
    <message>
        <location filename="../../CommandsGUI.py" line="993"/>
        <source>Wait</source>
        <translation>等待</translation>
    </message>
    <message>
        <location filename="../../CommandsGUI.py" line="994"/>
        <source>This command will wait for a certain amount of time. Time is measured in seconds.</source>
        <translation>设置等待时间（单位：秒）。</translation>
    </message>
    <message>
        <location filename="../../CommandsGUI.py" line="1005"/>
        <source>Number of seconds </source>
        <translation>秒数</translation>
    </message>
    <message>
        <location filename="../../CommandsGUI.py" line="1088"/>
        <source> seconds</source>
        <translation> 秒</translation>
    </message>
    <message>
        <location filename="../../CommandsGUI.py" line="1032"/>
        <source>Deactivate Gripper</source>
        <translation>关闭吸盘/夹子</translation>
    </message>
    <message>
        <location filename="../../CommandsGUI.py" line="1033"/>
        <source>Deactivates the robots gripper</source>
        <translation>停止吸取/夹取</translation>
    </message>
    <message>
        <location filename="../../CommandsGUI.py" line="1042"/>
        <source>Play Tone</source>
        <translation>播放声音</translation>
    </message>
    <message>
        <location filename="../../CommandsGUI.py" line="1043"/>
        <source>This tool uses the robots buzzer to play a tone at a certain frequency for a certain amount of time</source>
        <translation>让机械臂的蜂鸣器发声。你可以设置音调高低，及播放时间</translation>
    </message>
    <message>
        <location filename="../../CommandsGUI.py" line="1059"/>
        <source>Frequency </source>
        <translation>频率（数值越大，音调越高）</translation>
    </message>
    <message>
        <location filename="../../CommandsGUI.py" line="1060"/>
        <source>Duration </source>
        <translation>发声时长</translation>
    </message>
    <message>
        <location filename="../../CommandsGUI.py" line="1061"/>
        <source>Wait </source>
        <translation>等待</translation>
    </message>
    <message>
        <location filename="../../CommandsGUI.py" line="1087"/>
        <source>Play a tone of </source>
        <translation>播放声音</translation>
    </message>
    <message>
        <location filename="../../CommandsGUI.py" line="1103"/>
        <source>Move Relative To Object</source>
        <translation>移动到物体</translation>
    </message>
    <message>
        <location filename="../../CommandsGUI.py" line="1550"/>
        <source>Choose an object </source>
        <translation>选择一个物体 </translation>
    </message>
    <message>
        <location filename="../../CommandsGUI.py" line="1193"/>
        <source>Set Wrist Relative To Object</source>
        <translation>随物体旋转吸盘</translation>
    </message>
    <message>
        <location filename="../../CommandsGUI.py" line="1216"/>
        <source>Choose an Object</source>
        <translation>选择一个需要识别的物体</translation>
    </message>
    <message>
        <location filename="../../CommandsGUI.py" line="1241"/>
        <source>Relative to X Axis </source>
        <translation>相对于 X 轴</translation>
    </message>
    <message>
        <location filename="../../CommandsGUI.py" line="1242"/>
        <source>Relative to Robot Base </source>
        <translation>相对于机械臂底部 </translation>
    </message>
    <message>
        <location filename="../../CommandsGUI.py" line="1262"/>
        <source>Set the wrist </source>
        <translation>吸盘相对该物体的 </translation>
    </message>
    <message>
        <location filename="../../CommandsGUI.py" line="1263"/>
        <source> degrees relative to </source>
        <translation>旋转角度为</translation>
    </message>
    <message>
        <location filename="../../CommandsGUI.py" line="1272"/>
        <source>Pick Up Object</source>
        <translation>捡起物体</translation>
    </message>
    <message>
        <location filename="../../CommandsGUI.py" line="1315"/>
        <source>Pick Up </source>
        <translation>捡起物体</translation>
    </message>
    <message>
        <location filename="../../CommandsGUI.py" line="1316"/>
        <source>Find </source>
        <translation>查找</translation>
    </message>
    <message>
        <location filename="../../CommandsGUI.py" line="1316"/>
        <source> and pick it up</source>
        <translation> 并捡起</translation>
    </message>
    <message>
        <location filename="../../CommandsGUI.py" line="1325"/>
        <source>Test If Object Seen</source>
        <translation>条件：若“看见”某物体</translation>
    </message>
    <message>
        <location filename="../../CommandsGUI.py" line="1346"/>
        <source>If recognized </source>
        <translation>如果“看见”</translation>
    </message>
    <message>
        <location filename="../../CommandsGUI.py" line="1347"/>
        <source>Confidence level </source>
        <translation>可信度 </translation>
    </message>
    <message>
        <location filename="../../CommandsGUI.py" line="1348"/>
        <source>When </source>
        <translation>当 </translation>
    </message>
    <message>
        <location filename="../../CommandsGUI.py" line="1449"/>
        <source>NOT</source>
        <translation>不</translation>
    </message>
    <message>
        <location filename="../../CommandsGUI.py" line="1514"/>
        <source>Test If </source>
        <translation>条件：若“看见”物体</translation>
    </message>
    <message>
        <location filename="../../CommandsGUI.py" line="1409"/>
        <source> Seen</source>
        <translation> </translation>
    </message>
    <message>
        <location filename="../../CommandsGUI.py" line="1413"/>
        <source>If</source>
        <translation>如果</translation>
    </message>
    <message>
        <location filename="../../CommandsGUI.py" line="1599"/>
        <source> NOT</source>
        <translation> 不</translation>
    </message>
    <message>
        <location filename="../../CommandsGUI.py" line="1415"/>
        <source> confident object was seen</source>
        <translation> 确信该物体被“看见”</translation>
    </message>
    <message>
        <location filename="../../CommandsGUI.py" line="1424"/>
        <source>Test If Object Inside Region</source>
        <translation>条件：如果物体在某区域范围里</translation>
    </message>
    <message>
        <location filename="../../CommandsGUI.py" line="1446"/>
        <source>Choose an Object </source>
        <translation>选择一个要识别的物体 </translation>
    </message>
    <message>
        <location filename="../../CommandsGUI.py" line="1447"/>
        <source>What part of object must enter the location </source>
        <translation>你想把该物体的哪部分放置在规定区域内？</translation>
    </message>
    <message>
        <location filename="../../CommandsGUI.py" line="1448"/>
        <source>Click and drag the area of the screen that the object will be in</source>
        <translation>请用鼠标拖拽出指定区域（如果物体被放置在该区域内，则执行接下来的命令）</translation>
    </message>
    <message>
        <location filename="../../CommandsGUI.py" line="1514"/>
        <source> Inside Region</source>
        <translation>在区域内</translation>
    </message>
    <message>
        <location filename="../../CommandsGUI.py" line="1755"/>
        <source>If </source>
        <translation>如果 </translation>
    </message>
    <message>
        <location filename="../../CommandsGUI.py" line="1517"/>
        <source> of </source>
        <translation> 在 </translation>
    </message>
    <message>
        <location filename="../../CommandsGUI.py" line="1756"/>
        <source> is</source>
        <translation> 是</translation>
    </message>
    <message>
        <location filename="../../CommandsGUI.py" line="1519"/>
        <source> seen within a region</source>
        <translation>被放置在该区域内</translation>
    </message>
    <message>
        <location filename="../../CommandsGUI.py" line="1528"/>
        <source>Test Angle Of Object</source>
        <translation>条件：如果物体的摆放角度为...</translation>
    </message>
    <message>
        <location filename="../../CommandsGUI.py" line="1594"/>
        <source>Test Angle of </source>
        <translation>条件：如果物体的摆放角度为...</translation>
    </message>
    <message>
        <location filename="../../CommandsGUI.py" line="1597"/>
        <source>If angle is</source>
        <translation>如果该物体的X轴</translation>
    </message>
    <message>
        <location filename="../../CommandsGUI.py" line="1600"/>
        <source> between (</source>
        <translation>和机械臂 X 轴的夹角为(</translation>
    </message>
    <message>
        <location filename="../../CommandsGUI.py" line="1601"/>
        <source>) degrees from the X Axis</source>
        <translation>) 度</translation>
    </message>
    <message>
        <location filename="../../CommandsGUI.py" line="1619"/>
        <source>This is the start of a block of commands that only run if a conditional statement is met.</source>
        <translation>若满足上述条件，则开始执行以下命令</translation>
    </message>
    <message>
        <location filename="../../CommandsGUI.py" line="1632"/>
        <source>This is the end of a block of commands.</source>
        <translation>上述命令到此为止。</translation>
    </message>
    <message>
        <location filename="../../CommandsGUI.py" line="1645"/>
        <source>This will run commands if a test evaluates to False</source>
        <translation>若不符合条件，则执行以下命令</translation>
    </message>
    <message>
        <location filename="../../CommandsGUI.py" line="1654"/>
        <source>Set Variable</source>
        <translation>设置变量</translation>
    </message>
    <message>
        <location filename="../../CommandsGUI.py" line="1655"/>
        <source>This command can create a variable or set an existing variable to a value or an expression.</source>
        <translation>你可创建一个变量，或为已存在的变量设置内容。</translation>
    </message>
    <message>
        <location filename="../../CommandsGUI.py" line="1671"/>
        <source>Variable Name </source>
        <translation>变量名称 </translation>
    </message>
    <message>
        <location filename="../../CommandsGUI.py" line="1727"/>
        <source>Expression </source>
        <translation>变量内容 </translation>
    </message>
    <message>
        <location filename="../../CommandsGUI.py" line="1704"/>
        <source>Test Value</source>
        <translation>检测值</translation>
    </message>
    <message>
        <location filename="../../CommandsGUI.py" line="1705"/>
        <source>This will allow/disallow code to run that is in blocked brackets below it IF the test is true.</source>
        <translation>如果检测到的值符合标准，则执行/跳过以下命令</translation>
    </message>
    <message>
        <location filename="../../CommandsGUI.py" line="1719"/>
        <source>Equal To</source>
        <translation>等于</translation>
    </message>
    <message>
        <location filename="../../CommandsGUI.py" line="1720"/>
        <source>Not Equal To</source>
        <translation>不等于</translation>
    </message>
    <message>
        <location filename="../../CommandsGUI.py" line="1721"/>
        <source>Greater Than</source>
        <translation>大于</translation>
    </message>
    <message>
        <location filename="../../CommandsGUI.py" line="1722"/>
        <source>Less Than</source>
        <translation>小于</translation>
    </message>
    <message>
        <location filename="../../CommandsGUI.py" line="1726"/>
        <source>Test </source>
        <translation>检测</translation>
    </message>
    <message>
        <location filename="../../CommandsGUI.py" line="1751"/>
        <source> equal to</source>
        <translation>等于</translation>
    </message>
    <message>
        <location filename="../../CommandsGUI.py" line="1752"/>
        <source> not equal to</source>
        <translation> 不等于</translation>
    </message>
    <message>
        <location filename="../../CommandsGUI.py" line="1753"/>
        <source> greater than</source>
        <translation> 大于</translation>
    </message>
    <message>
        <location filename="../../CommandsGUI.py" line="1754"/>
        <source> less than</source>
        <translation> 小于</translation>
    </message>
    <message>
        <location filename="../../CommandsGUI.py" line="1757"/>
        <source> then</source>
        <translation>那么</translation>
    </message>
    <message>
        <location filename="../../CommandsGUI.py" line="1766"/>
        <source>Loop While Test Is True</source>
        <translation>当满足条件时，循环执行命令</translation>
    </message>
    <message>
        <location filename="../../CommandsGUI.py" line="1801"/>
        <source>Choose a Test</source>
        <translation>选择一个检测项目</translation>
    </message>
    <message>
        <location filename="../../CommandsGUI.py" line="1859"/>
        <source>End Task</source>
        <translation>结束任务（包括所有事件）</translation>
    </message>
    <message>
        <location filename="../../CommandsGUI.py" line="1860"/>
        <source>When the code reaches this point, the program will end.</source>
        <translation>该任务内的所有事件终止运行</translation>
    </message>
    <message>
        <location filename="../../CommandsGUI.py" line="1869"/>
        <source>Exit Current Event</source>
        <translation>退出当前事件</translation>
    </message>
    <message>
        <location filename="../../CommandsGUI.py" line="1870"/>
        <source>When the code reaches this point, the program will not process the rest of this event.</source>
        <translation>该事件终止运行</translation>
    </message>
    <message>
        <location filename="../../CommandsGUI.py" line="1882"/>
        <source>Run Python Code</source>
        <translation>执行 Python 代码</translation>
    </message>
    <message>
        <location filename="../../CommandsGUI.py" line="1924"/>
        <source>Run Task</source>
        <translation>执行任务</translation>
    </message>
    <message>
        <location filename="../../CommandsGUI.py" line="1948"/>
        <source>

Make sure the task you run has an
</source>
        <translation>请务必在你的任务中
</translation>
    </message>
    <message>
        <location filename="../../CommandsGUI.py" line="1948"/>
        <source>&apos;End Task&apos; command in it, to return to
</source>
        <translation>加入“结束任务”命令
</translation>
    </message>
    <message>
        <location filename="../../CommandsGUI.py" line="1948"/>
        <source>this task when its finished</source>
        <translation>当该任务结束时</translation>
    </message>
    <message>
        <location filename="../../CommandsGUI.py" line="1956"/>
        <source>Select Task</source>
        <translation>选择任务</translation>
    </message>
    <message>
        <location filename="../../CommandsGUI.py" line="1960"/>
        <source>Share Current Tasks Variables</source>
        <translation>共享当前任务的变量</translation>
    </message>
    <message>
        <location filename="../../CommandsGUI.py" line="1982"/>
        <source>No Task Selected</source>
        <translation>没有选中任何任务</translation>
    </message>
    <message>
        <location filename="../../CommandsGUI.py" line="1984"/>
        <source>Run </source>
        <translation>执行 </translation>
    </message>
    <message>
        <location filename="../../CommandsGUI.py" line="2098"/>
        <source>Run Function</source>
        <translation>执行函数/自定义功能</translation>
    </message>
    <message>
        <location filename="../../CommandsGUI.py" line="2047"/>
        <source>Choose a Function </source>
        <translation>选择一个函数/自定义功能 </translation>
    </message>
    <message>
        <location filename="../../CommandsGUI.py" line="2097"/>
        <source>No function selected</source>
        <translation>没有选中函数/自定义功能</translation>
    </message>
    <message>
        <location filename="../../CommandsGUI.py" line="2112"/>
        <source>Vision Assisted Move XYZ</source>
        <translation>视觉辅助下移动到 (X,Y,Z)</translation>
    </message>
    <message>
        <location filename="../../CommandsGUI.py" line="2120"/>
        <source>This function is experimental. It may not yield more accurate results.</source>
        <translation>此功能还在开发中，效果有待改进。</translation>
    </message>
    <message>
        <location filename="../../CommandsGUI.py" line="747"/>
        <source>
                                                    This will play back a &apos;Movement recording&apos; at a playback speed of your choosing. To create robot
&quot;
                                                    movement recordings, simply click on &apos;Resources&apos; on the toolbar and add a new recording.
                                                    </source>
        <translation>根据你设置的速度来播放已录制的动作。
若想录制一段新动作，可进入“菜单栏－－素材库”进行录制。</translation>
    </message>
    <message>
        <location filename="../../CommandsGUI.py" line="812"/>
        <source>
                                                    This tool sets the speed of the robot for any move commands that are done after this. 

                                                    For example, if you set the speed to 20, then do two Move XYZ commands, the robot will move to 

                                                    those locations with a speed of 20 cm/s. The default robot speed is 10 cm/s.
                                                    </source>
        <translation>通过此工具，你可设置uArm的运动速度。
如：当你设置速度为“20”，并让uArm移动到某个位置(x,y,z)，
uArm会以20厘米/秒的速度运动到该位置。uArm的默认运动速度为10厘米/秒。</translation>
    </message>
    <message>
        <location filename="../../CommandsGUI.py" line="1104"/>
        <source>
                                                    This tool uses computer vision to recognize an object of your choice, and position the robot directly
                                                    
relative to this objects XYZ location. If XYZ = 0,0,0, the robot will move directly onto the object.
                                                    

If you don&apos;t want to set one of the robots axis, simply leave it empty. For example, put y and z

                                                    empty and x o 5 will set the robots x position to objX + 5 while keeping the current Y and Z the same.
                                                    </source>
        <translation>选择你想让uArm“看见”的物体，利用视觉识别来引导uArm移动到该物体的相对位置。
如：
1）若(x,y,z)=(0,0,0)，uArm会识别指定物体，并移动到该物体的正上方。
2）若(x,y,z)=( , ,5)，即只设置z值为5，不填写x和y值，uArm会识别指定物体，并移动到比该物体高5厘米的位置。</translation>
    </message>
    <message>
        <location filename="../../CommandsGUI.py" line="1194"/>
        <source>
                                                    This tool will look at the orientation of an object in the cameras view, and align the wrist with 

                                                    the rotation of the object. The rotation of the object is determined by the orientation that it was

                                                    in when the object was memorized. It&apos;s recommended to experiment around a bit with this function to

                                                    get a feel for how it works!
                                                    </source>
        <translation>选择你想让uArm“看见”的物体，让uArm根据该物体的旋转角度来转动吸盘。
通过此功能，你可以让uArm将多个物体整齐叠放。
不熟悉“角度”概念？试着旋转物体，看看吸盘是怎么跟着动的？你很快就会摸索出该功能的使用方法！

问：什么是物体摆放角度？
当你在素材库中创建视觉识别对象时，屏幕会显示该物体的三维坐标（蓝－x轴；红－y轴；绿－z轴）。
1）相对于uArm X轴的摆放角度：蓝色箭头（正方向）与uArmX轴的夹角
2）相对于uArm底座的摆放角度：在uArm底座中点和该物体中点间连一条线，这条线与蓝色箭头（正方向）的夹角。

若想了解详情，请见《用户指南》中的图示说明。</translation>
    </message>
    <message>
        <location filename="../../CommandsGUI.py" line="1273"/>
        <source>
                                                    This tool uses computer vision to recognize an object of your choice, and attempt to pick up the
                                                    
object. If the object cannot be found or picked up, then False will be returned
                                                    </source>
        <translation>选择你想让uArm“看见”的物体，让uArm“看见”后捡起该物体。</translation>
    </message>
    <message>
        <location filename="../../CommandsGUI.py" line="1326"/>
        <source>This command will allow code in blocked brackets below it to run IF the specified object has been recognized.</source>
        <translation>如果uArm“看见”某物体，则运行“上下箭头”之间的命令块。</translation>
    </message>
    <message>
        <location filename="../../CommandsGUI.py" line="1425"/>
        <source>
                                                    This command will allow code in blocked brackets below it to run IF the specified object has been
                                                    recognized and the objects location in a particular location.
                                                    </source>
        <translation>如果uArm“看见”某物体在指定区域内，则运行“上下箭头”之间的命令块。</translation>
    </message>
    <message>
        <location filename="../../CommandsGUI.py" line="1529"/>
        <source>
                                                    This command will allow code in blocked brackets below it to run IF the object&apos;s rotation is

                                                    between two angles. The angles are measured from the robots positive X axis, counter clockwise. The

                                                    positive X axis is 0 degrees, the positive Y axis is 90 degrees, the negative X axis is 180degrees,

                                                     and so on.
                                                        </source>
        <translation>让uArm“看见”某物体，若该物体的摆放角度在某个范围内（如：30－60度之间），则运行“上下箭头”之间的命令块。

问：什么是物体的摆放角度？
以uArm X轴正方向为起点，即0度，逆时针旋转至物体坐标的蓝箭头（正方向）所得到的角度。
如，当uArm X轴指向3点钟方向，物体的蓝箭头指向12点钟方向，则物体摆放角度为90度。</translation>
    </message>
    <message>
        <location filename="../../CommandsGUI.py" line="1767"/>
        <source>Repeat this section of commands while a certain test returns true. You can choose what type of test will be used.
</source>
        <translation>请设置一个条件。当这个条件被满足时，以下命令将被重复执行。</translation>
    </message>
    <message>
        <location filename="../../CommandsGUI.py" line="1883"/>
        <source>This tool will execute a script made by the user.
DO NOT RUN PROGRAMS WITH SCRIPTS WRITTEN BY OTHER
                                                    
USERS UNLESS YOU HAVE CHECKED THE SCRIPT AND KNOW WHAT YOU ARE DOING!</source>
        <translation>直接运行自己编写的代码
不建议直接运行别人编写的代码。如果你想这样做，务必在使用前检查一遍他/她写的代码。</translation>
    </message>
    <message>
        <location filename="../../CommandsGUI.py" line="1925"/>
        <source>This tool will run  another task file and run it inside of this task, until the &apos;End Task&apos;

                                                    command is called within the task, then it will return to the currently running task.

                                                    All tasks are preloaded when script is launched, so if a child class runs a parent class, an error

                                                    will be returned.</source>
        <translation>在本任务中运行其它任务。
如：在任务A中运行任务B，当运行到任务B中的“结束任务”命令时，任务B结束，uArm会继续执行任务A。</translation>
    </message>
    <message>
        <location filename="../../CommandsGUI.py" line="1994"/>
        <source>This will run a custom function that the user defines in the Resources menu. If the function has 

                                                    arguments, the user will be prompted to fill out the arguments</source>
        <translation>运行素材库中的函数/自定义功能。
如果函数/自定义功能中涉及变量，你需要填写变量的值。</translation>
    </message>
    <message>
        <location filename="../../CommandsGUI.py" line="2113"/>
        <source>This works like the normal Move XYZ command, but uses vision to verify the robots position and

                                                        perform a &apos;correction&apos; move after an initial move. 

                                                        This command requires Camera/Robot Calibrations to be done.</source>
        <translation>让uArm在“看见”的情况下移动到某位置。
完成视觉校正后才可使用此功能。</translation>
    </message>
    <message>
        <location filename="../../CommandsGUI.py" line="1897"/>
        <source>Description </source>
        <translation>描述 </translation>
    </message>
    <message>
        <location filename="../../CommandsGUI.py" line="1563"/>
        <source>Start Angle </source>
        <translation>开始角度 </translation>
    </message>
    <message>
        <location filename="../../CommandsGUI.py" line="1568"/>
        <source>End Angle </source>
        <translation>结束角度 </translation>
    </message>
    <message>
        <location filename="../../CommandsGUI.py" line="1179"/>
        <source>Move Relative To </source>
        <translation>移动到物体</translation>
    </message>
    <message>
        <location filename="../../CommandsGUI.py" line="1593"/>
        <source>Object</source>
        <translation> </translation>
    </message>
    <message>
        <location filename="../../CommandsGUI.py" line="1260"/>
        <source>Set Wrist Relative To </source>
        <translation>随物体旋转吸盘</translation>
    </message>
    <message>
        <location filename="../../CommandsGUI.py" line="1372"/>
        <source>When: </source>
        <translation>当： </translation>
    </message>
    <message>
        <location filename="../../CommandsGUI.py" line="1374"/>
        <source>Just now</source>
        <translation>刚好</translation>
    </message>
    <message>
        <location filename="../../CommandsGUI.py" line="1376"/>
        <source> frames</source>
        <translation>帧</translation>
    </message>
    <message>
        <location filename="../../CommandsGUI.py" line="1411"/>
        <source>slightly</source>
        <translation>低</translation>
    </message>
    <message>
        <location filename="../../CommandsGUI.py" line="1411"/>
        <source>fairly</source>
        <translation>中</translation>
    </message>
    <message>
        <location filename="../../CommandsGUI.py" line="1411"/>
        <source>highly</source>
        <translation>高</translation>
    </message>
    <message>
        <location filename="../../CommandsGUI.py" line="1334"/>
        <source>low</source>
        <translation>低</translation>
    </message>
    <message>
        <location filename="../../CommandsGUI.py" line="1334"/>
        <source>medium</source>
        <translation>中</translation>
    </message>
    <message>
        <location filename="../../CommandsGUI.py" line="1334"/>
        <source>high</source>
        <translation>高</translation>
    </message>
    <message>
        <location filename="../../CommandsGUI.py" line="1775"/>
        <source>Loops commands while a chosen test is true</source>
        <translation>如果条件被满足，则循环运行以下命令</translation>
    </message>
</context>
<context>
    <name>CommonGUI</name>
    <message>
        <location filename="../../CommonGUI.py" line="164"/>
        <source>
    Using this scripting module, the possibilities are endless. You can directly inject python code into your program
without a hassle. You can use any of the libraries and modules that are built into this software, real time, and
without any extra modification.

    There are certain classes that are loaded into the script as python builtins, so you don&apos;t need to pass them to
functions or worry about scope, or even worry about setting them global. They are:


Builtin Variables:
    robot
        You have full access to controlling the robot, using the Robot.py library that was built as a wrapper for
        a communication protocol.

        For source code on the Robot class, go to:
        https://github.com/apockill/uArmCreatorStudio/blob/master/Logic/Robot.py


    vision
        Using this module, you can easly and without hassle track objects that you have taught the software in the
        Resource manager, find their location real time, search for past &quot;tracks&quot; of the objects, and act based upon
        that information. You can clear tracked objects, add new ones, and generally use powerful premade computer
        vision functions that have been built into this software already.

        For source code on the Vision class, go to:
        https://github.com/apockill/uArmCreatorStudio/blob/master/Logic/Vision.py

    resources
        You can pull any &quot;objects&quot; that you have built using the Resource Manager. This means, for example,
        that you could request a Movement Recording and replay it, or request a Vision object and track it.

        For source code on the Object Manager class, go to:
        https://github.com/apockill/uArmCreatorStudio/blob/master/Logic/ObjectManager.py

    settings
        This is a python dictionary of the GUI settings. This includes things like calibrations for various things.
        Try doing print(settings) to see what it contains.


    scriptStopping()
        This is a function that returns True if the user has pressed the &quot;stop&quot; button on the top left. You can use
        this to check if your script should end, if you&apos;re doing long loops.

        For source code on the Interpreter environment that runs your script, go to:
        https://github.com/apockill/uArmCreatorStudio/blob/master/Logic/Interpreter.py

    sleep
        The usual python sleep variable has been replaced by one that will automatically stop sleeping when the user
        presses the &quot;stop script&quot; button on the GUI. So don&apos;t worry about writing blocking code, that&apos;s been handled!

Examples scripts using &apos;robot&apos;
    robot.setPos(x=0, y=15, z=15)  # This will set the robots position to XYZ(0, 15, 15)
    robot.setPos(x=0, wait=False)  # Allows your code to continue while the robot moves.
    robot.setPos(x=0)              # Will only set the x position, keeps the rest the same
    robot.setGripper(True)         # Turn on the pump. If false, it will deactivate the pump
    robot.setBuzzer(1500, 2)       # Play a tone through the robots buzzer. Parameters: Frequency, duration (seconds)
    robot.setSpeed(10)             # Sets speed for all future moves using robot.setPos. Speed set in cm/s
    robot.connected()              # Returns True if the robot is connected and working, False if not

    robot.getAngles()              # Returns the current angles of the robots servos: [servo0, servo1, servo2, servo3]
    robot.getCoords()              # Returns the current coordinate of the robot in [x, y, z] format
    robot.getTipSensor()           # Returns True or False, if the tip sensor on the robot is being pressed or not
    robot.getMoving()              # Returns True if the robot is currently moving



Example scripts using &apos;vision&apos;
    # The first step of using vision is getting a trackable object. Make an object in Resources then access it by name.
    trackableObject = resources.getObject(&quot;Ace of Spades&quot;)


    # The next step is to make sure vision is tracking the object. Usually this should be done in Initialization event.
    # Objects only stop being tracked when the script ends. Do this only once.
    vision.addPlaneTarget(trackableObject)


    # Wait two seconds to make sure that vision has time to search for the new object
    sleep(2)


    # Alternatively you can use the following, which will wait for 30 frames to pass before continuing
    vision.waitForNewFrames(30)


    # If the object is already being tracked and has been for a while, you can try using vision to search for it
    # This function returns how many frames ago the object was recognized, and a &quot;tracked&quot; object with some information
    frameID, trackedObject = vision.getObjectLatestRecognition(trackableObject)


    # If no object is found, the &quot;trackedObject&quot; will be None. Check if its None before continuing
    if trackedObject is None:
        # Handle the error here
        print(&quot;Object &quot;, trackableObject.name, &quot; was not recognized!&quot;)
        return

    # If the object was, in fact, found, then you can pull all sorts of information from it
    print(trackedObject.center)     # Prints a list [x, y, z] of the objects position in the cameras coordinate system
    print(trackedObject.rotation)   # Prints a list [xRotation, yRotation, zRotation] of rotation along each axis
    print(trackedObject.ptCount)    # Prints how many points the object was recognized with. More points = more accuracy


    # Here is another function for looking for tracked objects
    # This will search through the last 30 frames for trackableObject, and try to find a recognition with &gt; 50 keypoints
    trackedObject = vision.searchTrackedHistory(trackable=trackableObject, maxAge=30, minPoints=50)



Any variable created in the scope of the script command can be used in any other script command, or block command
    def someFunctionName(someArgument):
        # Any python function here
        print(&quot;This function can work in any script command in the task!&quot;)
        print(someArgument)

    someVariableName = &quot;This string can be used in any Script command in the program&quot;



You might notice that scripts with big loops or &apos;while True&apos; statements will take a long time to end when the &quot;stop&quot;
button is pressed on the GUI. Sometimes, they might freeze the program. The reason for this is because your code
is running inside of a seperate thread/process, and when you end the task the thread has to end as well.

Any drag-and-drop command will end quickly, because they have been designed to do so. However, you will have to do this
yourself if you have a long lasting script that you want to be able to quit at any time. In order to do so, you can use
the function &quot;scriptStopping()&quot;

scriptStopping() returns True if the user has attempted to end the task, and False if the task has not been ended

    The typical use case is:

    while [Some Condition]:
        if scriptStopping(): break  # Break out of the loop if the program has ended. Place this wherever needed
        # ... code ...
        # ... code ...
        # ... code ...

    or, if it&apos;s in a big loop

    for i in range(0, 100000):
        if scriptStopping(): break
        # ... code ...
        # ... code ...
        # ... code ...

</source>
        <translation type="obsolete">编程的可能性是无限的:D！欢迎直接用Python代码实现你脑海中的酷炫想法💡
同时，此软件为开发者们准备了内置的代码库和模组，欢迎使用！

</translation>
    </message>
    <message>
        <location filename="../../CommonGUI.py" line="164"/>
        <source>
    Using this scripting module, the possibilities are endless. You can directly inject python code into your program
without a hassle. You can use any of the libraries and modules that are built into this software, real time, and
without any extra modification.

    There are certain classes that are loaded into the script as python builtins, so you don&apos;t need to pass them to
functions or worry about scope, or even worry about setting them global. They are:


Builtin Variables:
    robot
        You have full access to controlling the robot, using the Robot.py library that was built as a wrapper for
        a communication protocol.

        For source code on the Robot class, go to:
        https://github.com/apockill/uArmCreatorStudio/blob/master/Logic/Robot.py


    vision
        Using this module, you can easly and without hassle track objects that you have taught the software in the
        Resource manager, find their location real time, search for past &quot;tracks&quot; of the objects, and act based upon
        that information. You can clear tracked objects, add new ones, and generally use powerful premade computer
        vision functions that have been built into this software already.

        For source code on the Vision class, go to:
        https://github.com/apockill/uArmCreatorStudio/blob/master/Logic/Vision.py

    resources
        You can pull any &quot;objects&quot; that you have built using the Resource Manager. This means, for example,
        that you could request a Movement Recording and replay it, or request a Vision object and track it.

        For source code on the Object Manager class, go to:
        https://github.com/apockill/uArmCreatorStudio/blob/master/Logic/ObjectManager.py

    settings
        This is a python dictionary of the GUI settings. This includes things like calibrations for various things.
        Try doing print(settings) to see what it contains.


    scriptStopping()
        This is a function that returns True if the user has pressed the &quot;stop&quot; button on the top left. You can use
        this to check if your script should end, if you&apos;re doing long loops.

        For source code on the Interpreter environment that runs your script, go to:
        https://github.com/apockill/uArmCreatorStudio/blob/master/Logic/Interpreter.py

    sleep
        The usual python sleep variable has been replaced by one that will automatically stop sleeping when the user
        presses the &quot;stop script&quot; button on the GUI. So don&apos;t worry about writing blocking code, that&apos;s been handled!

Examples scripts using &apos;robot&apos;
    robot.setPos(x=0, y=15, z=15)  # This will set the robots position to XYZ(0, 15, 15)
    robot.setPos(x=0, wait=False)  # Allows your code to continue while the robot moves.
    robot.setPos(x=0)              # Will only set the x position, keeps the rest the same
    robot.setPump(True)            # Turn on the pump. If false, it will deactivate the pump
    robot.setBuzzer(1500, 2)       # Play a tone through the robots buzzer. Parameters: Frequency, duration (seconds)
    robot.setSpeed(10)             # Sets speed for all future moves using robot.setPos. Speed set in cm/s
    robot.connected()              # Returns True if the robot is connected and working, False if not

    robot.getAngles()              # Returns the current angles of the robots servos: [servo0, servo1, servo2, servo3]
    robot.getCoords()              # Returns the current coordinate of the robot in [x, y, z] format
    robot.getTipSensor()           # Returns True or False, if the tip sensor on the robot is being pressed or not
    robot.getMoving()              # Returns True if the robot is currently moving



Example scripts using &apos;vision&apos;
    # The first step of using vision is getting a trackable object. Make an object in Resources then access it by name.
    trackableObject = resources.getObject(&quot;Ace of Spades&quot;)


    # The next step is to make sure vision is tracking the object. Usually this should be done in Initialization event.
    # Objects only stop being tracked when the script ends. Do this only once.
    vision.addPlaneTarget(trackableObject)


    # Wait two seconds to make sure that vision has time to search for the new object
    sleep(2)


    # Alternatively you can use the following, which will wait for 30 frames to pass before continuing
    vision.waitForNewFrames(30)


    # If the object is already being tracked and has been for a while, you can try using vision to search for it
    # This function returns how many frames ago the object was recognized, and a &quot;tracked&quot; object with some information
    frameID, trackedObject = vision.getObjectLatestRecognition(trackableObject)


    # If no object is found, the &quot;trackedObject&quot; will be None. Check if its None before continuing
    if trackedObject is None:
        # Handle the error here
        print(&quot;Object &quot;, trackableObject.name, &quot; was not recognized!&quot;)
        return

    # If the object was, in fact, found, then you can pull all sorts of information from it
    print(trackedObject.center)     # Prints a list [x, y, z] of the objects position in the cameras coordinate system
    print(trackedObject.rotation)   # Prints a list [xRotation, yRotation, zRotation] of rotation along each axis
    print(trackedObject.ptCount)    # Prints how many points the object was recognized with. More points = more accuracy


    # Here is another function for looking for tracked objects
    # This will search through the last 30 frames for trackableObject, and try to find a recognition with &gt; 50 keypoints
    trackedObject = vision.searchTrackedHistory(trackable=trackableObject, maxAge=30, minPoints=50)



Any variable created in the scope of the script command can be used in any other script command, or block command
    def someFunctionName(someArgument):
        # Any python function here
        print(&quot;This function can work in any script command in the task!&quot;)
        print(someArgument)

    someVariableName = &quot;This string can be used in any Script command in the program&quot;



You might notice that scripts with big loops or &apos;while True&apos; statements will take a long time to end when the &quot;stop&quot;
button is pressed on the GUI. Sometimes, they might freeze the program. The reason for this is because your code
is running inside of a seperate thread/process, and when you end the task the thread has to end as well.

Any drag-and-drop command will end quickly, because they have been designed to do so. However, you will have to do this
yourself if you have a long lasting script that you want to be able to quit at any time. In order to do so, you can use
the function &quot;scriptStopping()&quot;

scriptStopping() returns True if the user has attempted to end the task, and False if the task has not been ended

    The typical use case is:

    while [Some Condition]:
        if scriptStopping(): break  # Break out of the loop if the program has ended. Place this wherever needed
        # ... code ...
        # ... code ...
        # ... code ...

    or, if it&apos;s in a big loop

    for i in range(0, 100000):
        if scriptStopping(): break
        # ... code ...
        # ... code ...
        # ... code ...

</source>
        <translation type="obsolete">
    在脚本模式下你可以尽情发挥你的想象空间。你可以在你的项目里面直接注入 Python 代码但不用步署和配置任何环境。
你可以实时的使用任何内置的库或者模块，但不需要对 UCS 本身做任何修改。

    UCS 在打开的时候已经加载了常用的类，你不需要通过函数去调用，也不需要理会它是全局变量还是临时变量。总共有这些：

内置变量：
    robot - 机械臂
      你拥有全部的机械臂的访问权限，你可以直接使用 Robot.py 库封装了通信协议。

      你可以在这里找到相关的源代码：
      https://github.com/apockill/uArmCreatorStudio/blob/master/Logic/Robot.py

    vision - 视觉
      使用视觉模块，你可以不用再为追踪物体换算机械臂坐标而烦恼，并且你已经可以直接使用素材库里添加的视觉素材，并且
      可以实时查找他们的位置，最长还可以追踪 60 帧之前的物体。你可以清除追踪物体，并且重新添加，然后就可以像平常一
      样使用UCS内置好的的计算机视觉函数。

      你可以在这里找到相关的源代码：
      https://github.com/apockill/uArmCreatorStudio/blob/master/Logic/ObjectManager.py

    settings - 设置
      有关界面（GUI）的设置是存放在一个 python 的字典(dictionary)里。这里面包含了像校正之类的各种各样的信息。
      你可以尝试使用 print(settings) 来查看里面有些什么东西。

    scriptStopping() - 脚本停止
      这是帮助你在设计 Python 脚本时检测停止信号的一个函数，当用户在主工具栏按下 &quot;停止&quot; 按钮的时候，你可以使用这个函数
      来判断是否要终止你的脚本，特别是你在使用一个循环时。

      你可以在这里找到相关的源代码：
      https://github.com/apockill/uArmCreatorStudio/blob/master/Logic/Interpreter.py

    sleep - 休眠
      这跟 Python 内置的 sleep 函数(time.sleep)有点不太一样，它们的区别是，当用户按下 &quot;停止&quot; 按钮的时候，Sleep
      函数将会失效。你不用再去担心写阻塞代码会影响到整个程序，这个函数会处理好的。

&apos;robot&apos;脚本使用示例
      robot.setPos(x=0, y=15, z=15)     # 使机械臂移动到一个坐标 XYZ(0, 15, 15)
      robot.setPos(x=0, wait=False)     # 异步式移动
      robot.setPos(x=0)                 # 只会设置 x 的坐标，其它保持一致
      robot.setPump(True)               # 打开气泵（夹子），如果是 False 会关闭气泵（夹子）
      robot.setBuzzer(1500, 2)          # 可以使用机械臂内置的蜂鸣器播放一段音乐，第一个参数是频率，单位是 hz, 第二个是持续时间
      robot.setSpeed(10)                # 设置机械臂的运动速度
      robot.connected()                 # 如果机械臂已连接会返回 True
      robot.getAngles()                 # 返回当前机械臂的电机角度 [servo0, servo1, servo2, servo3]
      robot.getCoords()                 # 返回当前机械臂的空间坐标 [x, y, z]
      robot.getTipSensor()              # 返回限位开关的状态 True or False
      robot.getMoving()                 # 返回当前机械臂的运动情况 True or False

&apos;vision&apos; 脚本使用示例
      # 使用视觉的第一步是获取一个追踪物体。先在素材库添加一个，然后你就可以在脚本中用名字访问它。
      trackableObject = resources.getObject(&quot;Ace of Spades&quot;)

      # 下一步，确保视觉正在追踪这个物体。通常这会在初始化事件里面完成。
      # 物体只会在脚本终止的时候才会停止被追踪。这个函数只用执行一次。
      vision.addPlaneTarget(trackableObject)

      # 等待两秒来确保视觉有足够的时间去查找这个新物体
      sleep(2)

      # 你可以选择使用下面的方式，等待 30 帧再继续
      vision.waitForNewFrames(30)

      # 如果物体是已经被追踪过有一段时间的，你可以尝试用视觉来寻找它
      # 这个函数会返回物体被识别之前总共有多少帧，并且带有 &quot;被追踪的&quot; 物体的信息
      frameID, trackedObject = vision.getObjectLatestRecognition(trackableObject)

      # 如果没有找到物体，这个 &quot;trackedObject&quot; 将会是空 （None）。使用前请先检查是否为 空。
      if trackedObject is None:
          # 在这里处理错误
          print(&quot;Object &quot;, trackableObject.name, &quot; was not recognized!&quot;)
          return     
           
      # 如果这个物体真的被追踪到了，你可以在这里使用它的所有信息
      print(trackedObject.center)     # 打印这个物体在摄像头的空间坐标系以[x, y, z] 
      print(trackedObject.rotation)   # 打印每个轴的转角以[xRotation, yRotation, zRotation]
      print(trackedObject.ptCount)    # 打印有多少个点被识别，点数越多，越精确

      # 这是另外一个追踪物体的函数
      # 这个函数会查找 trackableObject 过去的 30 帧, 并且会找到识别点数大于 50 的帧。
      trackedObject = vision.searchTrackedHistory(trackable=trackableObject, maxAge=30, minPoints=50)


所有在脚本中创建的变量，都是全局的，意味着你可以在其它脚本，包括其它代码块中使用它们
    def someFunctionName(someArgument):
        # 随便写一个函数
        print(&quot;This function can work in any script command in the task!&quot;)
        print(someArgument)

    someVariableName = &quot;This string can be used in any Script command in the program&quot;

你也许已经注意到了，在按下 &quot;停止&quot; 按钮时，脚本如果在一个大循环或者 &apos;While True&apos; 的语句中退出需要等待一段很长的时间。
有时候，整个程序还会变得无响应。造成这个的原因是，你的代码是跑在一个独立的 线程/进程中的，当按下停止按钮的时候，线程也
必须停止。

任何拖拽命令设计成停止按钮按下时会立即停止。但是，你必须为你的脚本显式的退出以确保脚本可以快速终止。你可以使用上面我
们介绍的函数 &quot;scriptStopping()&quot;

通常使用的方式如下：

while [条件]:
    if scriptStopping(): break  # 使用 Break 可以帮助你快速的跳出程序。请无论如何都要使用这个。
    # ... 代码 ...
    # ... 代码 ...
    # ... 代码 ...

或者，在一个大循环中。

for i in range(0, 100000):
    if scriptStopping(): break
    # ... 代码 ...
    # ... 代码 ...
    # ... 代码 ...
</translation>
    </message>
    <message>
        <location filename="../../CommonGUI.py" line="165"/>
        <source>
  Using this scripting module, the possibilities are endless. You can directly inject python code into your program
without a hassle. You can use any of the libraries and modules that are built into this software, real time, and
without any extra modification.

  There are certain classes that are loaded into the script as python builtins, so you don&apos;t need to pass them to
functions or worry about scope, or even worry about setting them global. They are:


Builtin Variables:
  robot
      You have full access to controlling the robot, using the Robot.py library that was built as a wrapper for
      a communication protocol.

      For source code on the Robot class, go to:
      https://github.com/apockill/uArmCreatorStudio/blob/master/Logic/Robot.py


  vision
      Using this module, you can easly and without hassle track objects that you have taught the software in the
      Resource manager, find their location real time, search for past &quot;tracks&quot; of the objects, and act based upon
      that information. You can clear tracked objects, add new ones, and generally use powerful premade computer
      vision functions that have been built into this software already.

      For source code on the Vision class, go to:
      https://github.com/apockill/uArmCreatorStudio/blob/master/Logic/Vision.py

  resources
      You can pull any &quot;objects&quot; that you have built using the Resource Manager. This means, for example,
      that you could request a Movement Recording and replay it, or request a Vision object and track it.

      For source code on the Object Manager class, go to:
      https://github.com/apockill/uArmCreatorStudio/blob/master/Logic/ObjectManager.py

  settings
      This is a python dictionary of the GUI settings. This includes things like calibrations for various things.
      Try doing print(settings) to see what it contains.


  scriptStopping()
      This is a function that returns True if the user has pressed the &quot;stop&quot; button on the top left. You can use
      this to check if your script should end, if you&apos;re doing long loops.

      For source code on the Interpreter environment that runs your script, go to:
      https://github.com/apockill/uArmCreatorStudio/blob/master/Logic/Interpreter.py

  sleep
      The usual python sleep variable has been replaced by one that will automatically stop sleeping when the user
      presses the &quot;stop script&quot; button on the GUI. So don&apos;t worry about writing blocking code, that&apos;s been handled!

Examples scripts using &apos;robot&apos;
  robot.setPos(x=0, y=15, z=15)  # This will set the robots position to XYZ(0, 15, 15)
  robot.setPos(x=0, wait=False)  # Allows your code to continue while the robot moves.
  robot.setPos(x=0)              # Will only set the x position, keeps the rest the same
  robot.setPump(True)            # Turn on the pump. If false, it will deactivate the pump
  robot.setBuzzer(1500, 2)       # Play a tone through the robots buzzer. Parameters: Frequency, duration (seconds)
  robot.setSpeed(10)             # Sets speed for all future moves using robot.setPos. Speed set in cm/s
  robot.connected()              # Returns True if the robot is connected and working, False if not

  robot.getAngles()              # Returns the current angles of the robots servos: [servo0, servo1, servo2, servo3]
  robot.getCoords()              # Returns the current coordinate of the robot in [x, y, z] format
  robot.getTipSensor()           # Returns True or False, if the tip sensor on the robot is being pressed or not
  robot.getMoving()              # Returns True if the robot is currently moving



Example scripts using &apos;vision&apos;
  # The first step of using vision is getting a trackable object. Make an object in Resources then access it by name.
  trackableObject = resources.getObject(&quot;Ace of Spades&quot;)


  # The next step is to make sure vision is tracking the object. Usually this should be done in Initialization event.
  # Objects only stop being tracked when the script ends. Do this only once.
  vision.addPlaneTarget(trackableObject)


  # Wait two seconds to make sure that vision has time to search for the new object
  sleep(2)


  # Alternatively you can use the following, which will wait for 30 frames to pass before continuing
  vision.waitForNewFrames(30)


  # If the object is already being tracked and has been for a while, you can try using vision to search for it
  # This function returns how many frames ago the object was recognized, and a &quot;tracked&quot; object with some information
  frameID, trackedObject = vision.getObjectLatestRecognition(trackableObject)


  # If no object is found, the &quot;trackedObject&quot; will be None. Check if its None before continuing
  if trackedObject is None:
      # Handle the error here
      print(&quot;Object &quot;, trackableObject.name, &quot; was not recognized!&quot;)
      return

  # If the object was, in fact, found, then you can pull all sorts of information from it
  print(trackedObject.center)     # Prints a list [x, y, z] of the objects position in the cameras coordinate system
  print(trackedObject.rotation)   # Prints a list [xRotation, yRotation, zRotation] of rotation along each axis
  print(trackedObject.ptCount)    # Prints how many points the object was recognized with. More points = more accuracy


  # Here is another function for looking for tracked objects
  # This will search through the last 30 frames for trackableObject, and try to find a recognition with &gt; 50 keypoints
  trackedObject = vision.searchTrackedHistory(trackable=trackableObject, maxAge=30, minPoints=50)



Any variable created in the scope of the script command can be used in any other script command, or block command
  def someFunctionName(someArgument):
      # Any python function here
      print(&quot;This function can work in any script command in the task!&quot;)
      print(someArgument)

  someVariableName = &quot;This string can be used in any Script command in the program&quot;



You might notice that scripts with big loops or &apos;while True&apos; statements will take a long time to end when the &quot;stop&quot;
button is pressed on the GUI. Sometimes, they might freeze the program. The reason for this is because your code
is running inside of a seperate thread/process, and when you end the task the thread has to end as well.

Any drag-and-drop command will end quickly, because they have been designed to do so. However, you will have to do this
yourself if you have a long lasting script that you want to be able to quit at any time. In order to do so, you can use
the function &quot;scriptStopping()&quot;

scriptStopping() returns True if the user has attempted to end the task, and False if the task has not been ended

  The typical use case is:

  while [Some Condition]:
      if scriptStopping(): break  # Break out of the loop if the program has ended. Place this wherever needed
      # ... code ...
      # ... code ...
      # ... code ...

  or, if it&apos;s in a big loop

  for i in range(0, 100000):
      if scriptStopping(): break
      # ... code ...
      # ... code ...
      # ... code ...

</source>
        <translation type="obsolete">
    在脚本模式下你可以尽情发挥你的想象空间。你可以在你的项目里面直接注入 Python 代码但不用步署和配置任何环境。
你可以实时的使用任何内置的库或者模块，但不需要对 UCS 本身做任何修改。

    UCS 在打开的时候已经加载了常用的类，你不需要通过函数去调用，也不需要理会它是全局变量还是临时变量。总共有这些：

内置变量：
    robot - 机械臂
      你拥有全部的机械臂的访问权限，你可以直接使用 Robot.py 库封装了通信协议。

      你可以在这里找到相关的源代码：
      https://github.com/apockill/uArmCreatorStudio/blob/master/Logic/Robot.py

    vision - 视觉
      使用视觉模块，你可以不用再为追踪物体换算机械臂坐标而烦恼，并且你已经可以直接使用素材库里添加的视觉素材，并且
      可以实时查找他们的位置，最长还可以追踪 60 帧之前的物体。你可以清除追踪物体，并且重新添加，然后就可以像平常一
      样使用UCS内置好的的计算机视觉函数。

      你可以在这里找到相关的源代码：
      https://github.com/apockill/uArmCreatorStudio/blob/master/Logic/ObjectManager.py

    settings - 设置
      有关界面（GUI）的设置是存放在一个 python 的字典(dictionary)里。这里面包含了像校正之类的各种各样的信息。
      你可以尝试使用 print(settings) 来查看里面有些什么东西。

    scriptStopping() - 脚本停止
      这是帮助你在设计 Python 脚本时检测停止信号的一个函数，当用户在主工具栏按下 &quot;停止&quot; 按钮的时候，你可以使用这个函数
      来判断是否要终止你的脚本，特别是你在使用一个循环时。

      你可以在这里找到相关的源代码：
      https://github.com/apockill/uArmCreatorStudio/blob/master/Logic/Interpreter.py

    sleep - 休眠
      这跟 Python 内置的 sleep 函数(time.sleep)有点不太一样，它们的区别是，当用户按下 &quot;停止&quot; 按钮的时候，Sleep
      函数将会失效。你不用再去担心写阻塞代码会影响到整个程序，这个函数会处理好的。

&apos;robot&apos;脚本使用示例
      robot.setPos(x=0, y=15, z=15)     # 使机械臂移动到一个坐标 XYZ(0, 15, 15)
      robot.setPos(x=0, wait=False)     # 异步式移动
      robot.setPos(x=0)                 # 只会设置 x 的坐标，其它保持一致
      robot.setPump(True)               # 打开气泵（夹子），如果是 False 会关闭气泵（夹子）
      robot.setBuzzer(1500, 2)          # 可以使用机械臂内置的蜂鸣器播放一段音乐，第一个参数是频率，单位是 hz, 第二个是持续时间
      robot.setSpeed(10)                # 设置机械臂的运动速度
      robot.connected()                 # 如果机械臂已连接会返回 True
      robot.getAngles()                 # 返回当前机械臂的电机角度 [servo0, servo1, servo2, servo3]
      robot.getCoords()                 # 返回当前机械臂的空间坐标 [x, y, z]
      robot.getTipSensor()              # 返回限位开关的状态 True or False
      robot.getMoving()                 # 返回当前机械臂的运动情况 True or False

&apos;vision&apos; 脚本使用示例
      # 使用视觉的第一步是获取一个追踪物体。先在素材库添加一个，然后你就可以在脚本中用名字访问它。
      trackableObject = resources.getObject(&quot;Ace of Spades&quot;)

      # 下一步，确保视觉正在追踪这个物体。通常这会在初始化事件里面完成。
      # 物体只会在脚本终止的时候才会停止被追踪。这个函数只用执行一次。
      vision.addPlaneTarget(trackableObject)

      # 等待两秒来确保视觉有足够的时间去查找这个新物体
      sleep(2)

      # 你可以选择使用下面的方式，等待 30 帧再继续
      vision.waitForNewFrames(30)

      # 如果物体是已经被追踪过有一段时间的，你可以尝试用视觉来寻找它
      # 这个函数会返回物体被识别之前总共有多少帧，并且带有 &quot;被追踪的&quot; 物体的信息
      frameID, trackedObject = vision.getObjectLatestRecognition(trackableObject)

      # 如果没有找到物体，这个 &quot;trackedObject&quot; 将会是空 （None）。使用前请先检查是否为 空。
      if trackedObject is None:
          # 在这里处理错误
          print(&quot;Object &quot;, trackableObject.name, &quot; was not recognized!&quot;)
          return     
           
      # 如果这个物体真的被追踪到了，你可以在这里使用它的所有信息
      print(trackedObject.center)     # 打印这个物体在摄像头的空间坐标系以[x, y, z] 
      print(trackedObject.rotation)   # 打印每个轴的转角以[xRotation, yRotation, zRotation]
      print(trackedObject.ptCount)    # 打印有多少个点被识别，点数越多，越精确

      # 这是另外一个追踪物体的函数
      # 这个函数会查找 trackableObject 过去的 30 帧, 并且会找到识别点数大于 50 的帧。
      trackedObject = vision.searchTrackedHistory(trackable=trackableObject, maxAge=30, minPoints=50)


所有在脚本中创建的变量，都是全局的，意味着你可以在其它脚本，包括其它代码块中使用它们
    def someFunctionName(someArgument):
        # 随便写一个函数
        print(&quot;This function can work in any script command in the task!&quot;)
        print(someArgument)

    someVariableName = &quot;This string can be used in any Script command in the program&quot;

你也许已经注意到了，在按下 &quot;停止&quot; 按钮时，脚本如果在一个大循环或者 &apos;While True&apos; 的语句中退出需要等待一段很长的时间。
有时候，整个程序还会变得无响应。造成这个的原因是，你的代码是跑在一个独立的 线程/进程中的，当按下停止按钮的时候，线程也
必须停止。

任何拖拽命令设计成停止按钮按下时会立即停止。但是，你必须为你的脚本显式的退出以确保脚本可以快速终止。你可以使用上面我
们介绍的函数 &quot;scriptStopping()&quot;

通常使用的方式如下：

while [条件]:
    if scriptStopping(): break  # 使用 Break 可以帮助你快速的跳出程序。请无论如何都要使用这个。
    # ... 代码 ...
    # ... 代码 ...
    # ... 代码 ...

或者，在一个大循环中。

for i in range(0, 100000):
    if scriptStopping(): break
    # ... 代码 ...
    # ... 代码 ...
    # ... 代码 ...
</translation>
    </message>
    <message>
        <location filename="../../CommonGUI.py" line="165"/>
        <source>
Using this scripting module, the possibilities are endless. You can directly inject python code into your program without a hassle. You can use any of the libraries and modules that are built into this software, real time, and without any extra modification.

There are certain classes that are loaded into the script as python builtins, so you don&apos;t need to pass them to functions or worry about scope, or even worry about setting them global.

Important tips:
Any variable created in the scope of the script command can be used in any other script command, or block command
    def someFunctionName(someArgument):
        # Any python function here
        print(&quot;This function can work in any script command in the task!&quot;)
        print(someArgument)

    someVariableName = &quot;This string can be used in any Script command in the program&quot;


Types of built-in variables:
robot
vision
resources
settings
scriptStopping()
sleep

Detailed description:

robot

You have full access to controlling the robot, using the Robot.py library that was built as a wrapper for a communication protocol.

        For source code on the Robot class, go to:
        https://github.com/apockill/uArmCreatorStudio/blob/master/Logic/Robot.py

Examples scripts using &apos;robot&apos;
    robot.setPos(x=0, y=15, z=15)  # This will set the robots position to XYZ(0, 15, 15)
    robot.setPos(x=0, wait=False)  # Allows your code to continue while the robot moves.
    robot.setPos(x=0)              # Will only set the x position, keeps the rest the same
    robot.setGripper(True)         # Turn on the pump. If false, it will deactivate the pump
    robot.setBuzzer(1500, 2)       # Play a tone through the robots buzzer. Parameters: Frequency, duration (seconds)
    robot.setSpeed(10)             # Sets speed for all future moves using robot.setPos. Speed set in cm/s
    robot.connected()              # Returns True if the robot is connected and working, False if not

    robot.getAngles()              # Returns the current angles of the robots servos: [servo0, servo1, servo2, servo3]
    robot.getCoords()              # Returns the current coordinate of the robot in [x, y, z] format
    robot.getTipSensor()           # Returns True or False, if the tip sensor on the robot is being pressed or not
    robot.getMoving()              # Returns True if the robot is currently moving


2. vision

Using this module, you can easly and without hassle track objects that you have taught the software in the Resource manager, find their location real time, search for past &quot;tracks&quot; of the objects, and act based upon that information.

You can clear tracked objects, add new ones, and generally use powerful pre-made computer vision functions that have been built into this software already.

For source code on the Vision class, go to:
https://github.com/apockill/uArmCreatorStudio/blob/master/Logic/Vision.py

Example scripts using &apos;vision&apos;
    # The first step of using vision is getting a trackable object. Make an object in Resources then access it by name.
    trackableObject = resources.getObject(&quot;Ace of Spades&quot;)


    # The next step is to make sure vision is tracking the object. Usually this should be done in Initialization event.
    # Objects only stop being tracked when the script ends. Do this only once.
    vision.addPlaneTarget(trackableObject)


    # Wait two seconds to make sure that vision has time to search for the new object
    sleep(2)


    # Alternatively you can use the following, which will wait for 30 frames to pass before continuing
    vision.waitForNewFrames(30)


    # If the object is already being tracked and has been for a while, you can try using vision to search for it
    # This function returns how many frames ago the object was recognized, and a &quot;tracked&quot; object with some information
    frameID, trackedObject = vision.getObjectLatestRecognition(trackableObject)


    # If no object is found, the &quot;trackedObject&quot; will be None. Check if its None before continuing
    if trackedObject is None:
        # Handle the error here
        print(&quot;Object &quot;, trackableObject.name, &quot; was not recognized!&quot;)
        return

    # If the object was, in fact, found, then you can pull all sorts of information from it
    print(trackedObject.center)     # Prints a list [x, y, z] of the objects position in the cameras coordinate system
    print(trackedObject.rotation)   # Prints a list [xRotation, yRotation, zRotation] of rotation along each axis
    print(trackedObject.ptCount)    # Prints how many points the object was recognized with. More points = more accuracy


    # Here is another function for looking for tracked objects
    # This will search through the last 30 frames for trackableObject, and try to find a recognition with &gt; 50 keypoints
    trackedObject = vision.searchTrackedHistory(trackable=trackableObject, maxAge=30, minPoints=50)



3. resources

You can pull any &quot;objects&quot; that you have built using the Resource Manager.
This means, for example, that you could request a Movement Recording and replay it, or request a Vision object and track it.

For source code on the Object Manager class, go to:
https://github.com/apockill/uArmCreatorStudio/blob/master/Logic/ObjectManager.py

4. settings

This is a python dictionary of the GUI settings. This includes things like calibrations for various things.
 Try doing print(settings) to see what it contains.

5. scriptStopping()

This is a function that returns True if the user has pressed the &quot;stop&quot; button on the top left. You can use this to check if your script should end, if you&apos;re doing long loops.

For source code on the Interpreter environment that runs your script, go to:
https://github.com/apockill/uArmCreatorStudio/blob/master/Logic/Interpreter.py

You might notice that scripts with big loops or &apos;while True&apos; statements will take a long time to end when the “stop&quot; button is pressed on the GUI. Sometimes, they might freeze the program. The reason for this is because your code is running inside of a seperate thread/process, and when you end the task the thread has to end as well.

Any drag-and-drop command will end quickly, because they have been designed to do so. However, you will have to do this yourself if you have a long lasting script that you want to be able to quit at any time. In order to do so, you can use the function &quot;scriptStopping()&quot;

scriptStopping() returns True if the user has attempted to end the task, and False if the task has not been ended

    The typical use case is:

    while [Some Condition]:
        if scriptStopping(): break  # Break out of the loop if the program has ended. Place this wherever needed
        # ... code ...
        # ... code ...
        # ... code ...

    or, if it&apos;s in a big loop

    for i in range(0, 100000):

6. sleep

The usual python sleep variable has been replaced by one that will automatically stop sleeping when the user presses the &quot;stop script&quot; button on the GUI. So don&apos;t worry about writing blocking code, that&apos;s been handled!

</source>
        <translation>
    在脚本模式下你可以尽情发挥你的想象空间。你可以在你的项目里面直接注入 Python 代码但不用步署和配置任何环境。
你可以实时的使用任何内置的库或者模块，但不需要对 UCS 本身做任何修改。

    UCS 在打开的时候已经加载了常用的类，你不需要通过函数去调用，也不需要理会它是全局变量还是临时变量。总共有这些：

内置变量：
    robot - 机械臂
      你拥有全部的机械臂的访问权限，你可以直接使用 Robot.py 库封装了通信协议。

      你可以在这里找到相关的源代码：
      https://github.com/apockill/uArmCreatorStudio/blob/master/Logic/Robot.py

    vision - 视觉
      使用视觉模块，你可以不用再为追踪物体换算机械臂坐标而烦恼，并且你已经可以直接使用素材库里添加的视觉素材，并且
      可以实时查找他们的位置，最长还可以追踪 60 帧之前的物体。你可以清除追踪物体，并且重新添加，然后就可以像平常一
      样使用UCS内置好的的计算机视觉函数。

      你可以在这里找到相关的源代码：
      https://github.com/apockill/uArmCreatorStudio/blob/master/Logic/ObjectManager.py

    settings - 设置
      有关界面（GUI）的设置是存放在一个 python 的字典(dictionary)里。这里面包含了像校正之类的各种各样的信息。
      你可以尝试使用 print(settings) 来查看里面有些什么东西。

    scriptStopping() - 脚本停止
      这是帮助你在设计 Python 脚本时检测停止信号的一个函数，当用户在主工具栏按下 &quot;停止&quot; 按钮的时候，你可以使用这个函数
      来判断是否要终止你的脚本，特别是你在使用一个循环时。

      你可以在这里找到相关的源代码：
      https://github.com/apockill/uArmCreatorStudio/blob/master/Logic/Interpreter.py

    sleep - 休眠
      这跟 Python 内置的 sleep 函数(time.sleep)有点不太一样，它们的区别是，当用户按下 &quot;停止&quot; 按钮的时候，Sleep
      函数将会失效。你不用再去担心写阻塞代码会影响到整个程序，这个函数会处理好的。

&apos;robot&apos;脚本使用示例
      robot.setPos(x=0, y=15, z=15)     # 使机械臂移动到一个坐标 XYZ(0, 15, 15)
      robot.setPos(x=0, wait=False)     # 异步式移动
      robot.setPos(x=0)                 # 只会设置 x 的坐标，其它保持一致
      robot.setPump(True)               # 打开气泵（夹子），如果是 False 会关闭气泵（夹子）
      robot.setBuzzer(1500, 2)          # 可以使用机械臂内置的蜂鸣器播放一段音乐，第一个参数是频率，单位是 hz, 第二个是持续时间
      robot.setSpeed(10)                # 设置机械臂的运动速度
      robot.connected()                 # 如果机械臂已连接会返回 True
      robot.getAngles()                 # 返回当前机械臂的电机角度 [servo0, servo1, servo2, servo3]
      robot.getCoords()                 # 返回当前机械臂的空间坐标 [x, y, z]
      robot.getTipSensor()              # 返回限位开关的状态 True or False
      robot.getMoving()                 # 返回当前机械臂的运动情况 True or False

&apos;vision&apos; 脚本使用示例
      # 使用视觉的第一步是获取一个追踪物体。先在素材库添加一个，然后你就可以在脚本中用名字访问它。
      trackableObject = resources.getObject(&quot;Ace of Spades&quot;)

      # 下一步，确保视觉正在追踪这个物体。通常这会在初始化事件里面完成。
      # 物体只会在脚本终止的时候才会停止被追踪。这个函数只用执行一次。
      vision.addPlaneTarget(trackableObject)

      # 等待两秒来确保视觉有足够的时间去查找这个新物体
      sleep(2)

      # 你可以选择使用下面的方式，等待 30 帧再继续
      vision.waitForNewFrames(30)

      # 如果物体是已经被追踪过有一段时间的，你可以尝试用视觉来寻找它
      # 这个函数会返回物体被识别之前总共有多少帧，并且带有 &quot;被追踪的&quot; 物体的信息
      frameID, trackedObject = vision.getObjectLatestRecognition(trackableObject)

      # 如果没有找到物体，这个 &quot;trackedObject&quot; 将会是空 （None）。使用前请先检查是否为 空。
      if trackedObject is None:
          # 在这里处理错误
          print(&quot;Object &quot;, trackableObject.name, &quot; was not recognized!&quot;)
          return     
           
      # 如果这个物体真的被追踪到了，你可以在这里使用它的所有信息
      print(trackedObject.center)     # 打印这个物体在摄像头的空间坐标系以[x, y, z] 
      print(trackedObject.rotation)   # 打印每个轴的转角以[xRotation, yRotation, zRotation]
      print(trackedObject.ptCount)    # 打印有多少个点被识别，点数越多，越精确

      # 这是另外一个追踪物体的函数
      # 这个函数会查找 trackableObject 过去的 30 帧, 并且会找到识别点数大于 50 的帧。
      trackedObject = vision.searchTrackedHistory(trackable=trackableObject, maxAge=30, minPoints=50)


所有在脚本中创建的变量，都是全局的，意味着你可以在其它脚本，包括其它代码块中使用它们
    def someFunctionName(someArgument):
        # 随便写一个函数
        print(&quot;This function can work in any script command in the task!&quot;)
        print(someArgument)

    someVariableName = &quot;This string can be used in any Script command in the program&quot;

你也许已经注意到了，在按下 &quot;停止&quot; 按钮时，脚本如果在一个大循环或者 &apos;While True&apos; 的语句中退出需要等待一段很长的时间。
有时候，整个程序还会变得无响应。造成这个的原因是，你的代码是跑在一个独立的 线程/进程中的，当按下停止按钮的时候，线程也
必须停止。

任何拖拽命令设计成停止按钮按下时会立即停止。但是，你必须为你的脚本显式的退出以确保脚本可以快速终止。你可以使用上面我
们介绍的函数 &quot;scriptStopping()&quot;

通常使用的方式如下：

while [条件]:
    if scriptStopping(): break  # 使用 Break 可以帮助你快速的跳出程序。请无论如何都要使用这个。
    # ... 代码 ...
    # ... 代码 ...
    # ... 代码 ...

或者，在一个大循环中。

for i in range(0, 100000):
    if scriptStopping(): break
    # ... 代码 ...
    # ... 代码 ...
    # ... 代码 ...
</translation>
    </message>
</context>
<context>
    <name>Console</name>
    <message>
        <location filename="../../CommonGUI.py" line="451"/>
        <source>Run Code: </source>
        <translation>执行代码： </translation>
    </message>
    <message>
        <location filename="../../CommonGUI.py" line="578"/>
        <source>Console Settings</source>
        <translation>控制台设置</translation>
    </message>
    <message>
        <location filename="../../CommonGUI.py" line="580"/>
        <source>Here you can change settings about what you see in the console</source>
        <translation>请自定义你想在控制台中看到的信息</translation>
    </message>
    <message>
        <location filename="../../CommonGUI.py" line="584"/>
        <source>Customize what you see printed on the Console</source>
        <translation>自定义你能在控制台看到的信息</translation>
    </message>
    <message>
        <location filename="../../CommonGUI.py" line="586"/>
        <source>Wrap Lines </source>
        <translation>代码换行 </translation>
    </message>
    <message>
        <location filename="../../CommonGUI.py" line="587"/>
        <source>Robot Logs </source>
        <translation>uArm日志</translation>
    </message>
    <message>
        <location filename="../../CommonGUI.py" line="588"/>
        <source>Vision Logs </source>
        <translation>视觉日志 </translation>
    </message>
    <message>
        <location filename="../../CommonGUI.py" line="589"/>
        <source>Communication Logs </source>
        <translation>通信日志 </translation>
    </message>
    <message>
        <location filename="../../CommonGUI.py" line="590"/>
        <source>Interpreter Logs </source>
        <translation>解析器日志 </translation>
    </message>
    <message>
        <location filename="../../CommonGUI.py" line="591"/>
        <source>Script Logs </source>
        <translation>脚本日志 </translation>
    </message>
    <message>
        <location filename="../../CommonGUI.py" line="592"/>
        <source>GUI Logs </source>
        <translation>GUI(图形化界面)日志 </translation>
    </message>
    <message>
        <location filename="../../CommonGUI.py" line="593"/>
        <source>Other Logs </source>
        <translation>其它日志 </translation>
    </message>
    <message>
        <location filename="../../CommonGUI.py" line="594"/>
        <source>Save to File</source>
        <translation>保存到文件</translation>
    </message>
</context>
<context>
    <name>ControlPanel</name>
    <message>
        <location filename="../../ControlPanelGUI.py" line="151"/>
        <source>Command List</source>
        <translation>命令列表</translation>
    </message>
    <message>
        <location filename="../../ControlPanelGUI.py" line="82"/>
        <source>Add Event</source>
        <translation>添加事件</translation>
    </message>
    <message>
        <location filename="../../ControlPanelGUI.py" line="83"/>
        <source>Delete</source>
        <translation>删除</translation>
    </message>
    <message>
        <location filename="../../ControlPanelGUI.py" line="84"/>
        <source>Change</source>
        <translation>修改</translation>
    </message>
    <message>
        <location filename="../../ControlPanelGUI.py" line="157"/>
        <source> Command List</source>
        <translation> 命令列表</translation>
    </message>
    <message>
        <location filename="../../ControlPanelGUI.py" line="242"/>
        <source>Warning</source>
        <translation>警告</translation>
    </message>
</context>
<context>
    <name>CoordWizard</name>
    <message>
        <location filename="../../CalibrationsGUI.py" line="348"/>
        <source>Coordinate Calibration Wizard</source>
        <translation>坐标校正向导</translation>
    </message>
</context>
<context>
    <name>DeviceWindow</name>
    <message>
        <location filename="../../MainGUI.py" line="818"/>
        <source>Please select the robot you will be using:</source>
        <translation>请选择你正在使用的uArm端口：</translation>
    </message>
    <message>
        <location filename="../../MainGUI.py" line="816"/>
        <source>Please select the camera you will be using:</source>
        <translation>请选择你正在使用的摄像头：</translation>
    </message>
    <message>
        <location filename="../../MainGUI.py" line="819"/>
        <source>Scan for Robots</source>
        <translation>查找uArm</translation>
    </message>
    <message>
        <location filename="../../MainGUI.py" line="817"/>
        <source>Scan for Cameras</source>
        <translation>查找摄像头</translation>
    </message>
    <message>
        <location filename="../../MainGUI.py" line="849"/>
        <source>Apply</source>
        <translation>应用</translation>
    </message>
    <message>
        <location filename="../../MainGUI.py" line="850"/>
        <source>Cancel</source>
        <translation>取消</translation>
    </message>
    <message>
        <location filename="../../MainGUI.py" line="909"/>
        <source>Devices</source>
        <translation>设备</translation>
    </message>
    <message>
        <location filename="../../MainGUI.py" line="928"/>
        <source>No devices were found.</source>
        <translation>没有找到设备。</translation>
    </message>
    <message>
        <location filename="../../MainGUI.py" line="941"/>
        <source>Camera </source>
        <translation>摄像头 </translation>
    </message>
    <message>
        <location filename="../../MainGUI.py" line="948"/>
        <source>No cameras were found.</source>
        <translation>没有找到摄像头。</translation>
    </message>
    <message>
        <location filename="../../MainGUI.py" line="821"/>
        <source>Disconnect</source>
        <translation>断开连接</translation>
    </message>
    <message>
        <location filename="../../MainGUI.py" line="820"/>
        <source>Connected to Robot {}:</source>
        <translation type="obsolete">已连接到机械臂设备：</translation>
    </message>
    <message>
        <location filename="../../MainGUI.py" line="833"/>
        <source>Connected to Camera {}</source>
        <translation type="obsolete">已连接到摄像头设备：</translation>
    </message>
    <message>
        <location filename="../../MainGUI.py" line="822"/>
        <source>Connected to Camera {}:</source>
        <translation type="obsolete">已连接到摄像头设备：</translation>
    </message>
    <message>
        <location filename="../../MainGUI.py" line="820"/>
        <source>Connected to Robot:</source>
        <translation>已连接到机械臂设备：</translation>
    </message>
    <message>
        <location filename="../../MainGUI.py" line="822"/>
        <source>Connected to Camera:</source>
        <translation>已连接到摄像头设备：</translation>
    </message>
</context>
<context>
    <name>EventPromptWindow</name>
    <message>
        <location filename="../../EventsGUI.py" line="134"/>
        <source>Initialization</source>
        <translation>初始事件</translation>
    </message>
    <message>
        <location filename="../../EventsGUI.py" line="135"/>
        <source>Step</source>
        <translation>循环运行</translation>
    </message>
    <message>
        <location filename="../../EventsGUI.py" line="136"/>
        <source>Tip Sensor</source>
        <translation>按压吸盘控制</translation>
    </message>
    <message>
        <location filename="../../EventsGUI.py" line="137"/>
        <source>Keyboard</source>
        <translation>键盘控制</translation>
    </message>
    <message>
        <location filename="../../EventsGUI.py" line="138"/>
        <source>Motion Detected</source>
        <translation>运动检测</translation>
    </message>
    <message>
        <location filename="../../EventsGUI.py" line="139"/>
        <source>Recognized</source>
        <translation>视觉识别</translation>
    </message>
    <message>
        <location filename="../../EventsGUI.py" line="140"/>
        <source>Not Recognized</source>
        <translation>视觉未识别</translation>
    </message>
    <message>
        <location filename="../../EventsGUI.py" line="164"/>
        <source>Letters</source>
        <translation>字母</translation>
    </message>
    <message>
        <location filename="../../EventsGUI.py" line="174"/>
        <source>Digits</source>
        <translation>数字</translation>
    </message>
    <message>
        <location filename="../../EventsGUI.py" line="190"/>
        <source>No Motion</source>
        <translation>无动作</translation>
    </message>
    <message>
        <location filename="../../EventsGUI.py" line="191"/>
        <source>Any Motion</source>
        <translation>任何动作</translation>
    </message>
    <message>
        <location filename="../../EventsGUI.py" line="193"/>
        <source>Above &apos;High&apos; Speed</source>
        <translation>高速运动</translation>
    </message>
    <message>
        <location filename="../../EventsGUI.py" line="194"/>
        <source>Less than &apos;High&apos; Speed</source>
        <translation>中速运动</translation>
    </message>
    <message>
        <location filename="../../EventsGUI.py" line="196"/>
        <source>Between &apos;Low&apos; to &apos;High&apos; Speed</source>
        <translation>低速运动</translation>
    </message>
    <message>
        <location filename="../../EventsGUI.py" line="212"/>
        <source>Face Detected</source>
        <translation>人脸识别</translation>
    </message>
    <message>
        <location filename="../../EventsGUI.py" line="213"/>
        <source>Face Not Detected</source>
        <translation>没识别到人脸</translation>
    </message>
    <message>
        <location filename="../../EventsGUI.py" line="214"/>
        <source>Smile Detected</source>
        <translation>微笑识别</translation>
    </message>
    <message>
        <location filename="../../EventsGUI.py" line="215"/>
        <source>Smile Not Detected</source>
        <translation>没识别到微笑</translation>
    </message>
    <message>
        <location filename="../../EventsGUI.py" line="216"/>
        <source>Eye Detected</source>
        <translation>人眼识别</translation>
    </message>
    <message>
        <location filename="../../EventsGUI.py" line="217"/>
        <source>Eye Not Detected</source>
        <translation>没识别到人眼</translation>
    </message>
    <message>
        <location filename="../../EventsGUI.py" line="122"/>
        <source>Add an Event</source>
        <translation>添加一个事件</translation>
    </message>
    <message>
        <location filename="../../EventsGUI.py" line="127"/>
        <source>Cancel</source>
        <translation>取消</translation>
    </message>
</context>
<context>
    <name>EventWidget</name>
    <message>
        <location filename="../../EventsGUI.py" line="42"/>
        <source>No icon found.</source>
        <translation>未找到图标。</translation>
    </message>
</context>
<context>
    <name>EventsGUI</name>
    <message>
        <location filename="../../EventsGUI.py" line="314"/>
        <source>Initialization</source>
        <translation>初始事件</translation>
    </message>
    <message>
        <location filename="../../EventsGUI.py" line="315"/>
        <source>Activates once each time the task is run</source>
        <translation>任务开始后，仅运行1次右边的命令</translation>
    </message>
    <message>
        <location filename="../../EventsGUI.py" line="326"/>
        <source>Step</source>
        <translation>循环运行</translation>
    </message>
    <message>
        <location filename="../../EventsGUI.py" line="327"/>
        <source>Activates every time the events are refreshed</source>
        <translation>任务开始后，重复运行右边的命令</translation>
    </message>
    <message>
        <location filename="../../EventsGUI.py" line="341"/>
        <source>Tip Pressed</source>
        <translation>按压uArm吸盘</translation>
    </message>
    <message>
        <location filename="../../EventsGUI.py" line="342"/>
        <source>Activates when the sensor on the tip of the arm is pressed</source>
        <translation>当按压uArm末端吸盘时，运行右边的命令</translation>
    </message>
    <message>
        <location filename="../../EventsGUI.py" line="355"/>
        <source>Key Pressed</source>
        <translation>按键</translation>
    </message>
    <message>
        <location filename="../../EventsGUI.py" line="358"/>
        <source>KeyPress </source>
        <translation>按键 </translation>
    </message>
    <message>
        <location filename="../../EventsGUI.py" line="360"/>
        <source>Keypress </source>
        <translation>按键 </translation>
    </message>
    <message>
        <location filename="../../EventsGUI.py" line="361"/>
        <source>Activates when the letter </source>
        <translation>当输入字母 </translation>
    </message>
    <message>
        <location filename="../../EventsGUI.py" line="361"/>
        <source> is pressed</source>
        <translation> 时运行右边的命令</translation>
    </message>
    <message>
        <location filename="../../EventsGUI.py" line="376"/>
        <source>Motion Detected</source>
        <translation>动作检测</translation>
    </message>
    <message>
        <location filename="../../EventsGUI.py" line="382"/>
        <source>Above </source>
        <translation>高于 </translation>
    </message>
    <message>
        <location filename="../../EventsGUI.py" line="384"/>
        <source> Speed</source>
        <translation> 速度</translation>
    </message>
    <message>
        <location filename="../../EventsGUI.py" line="384"/>
        <source>Less than </source>
        <translation>小于 </translation>
    </message>
    <message>
        <location filename="../../EventsGUI.py" line="387"/>
        <source>Low to High Speed</source>
        <translation>低速</translation>
    </message>
    <message>
        <location filename="../../EventsGUI.py" line="391"/>
        <source>Any Motion</source>
        <translation>任何动作</translation>
    </message>
    <message>
        <location filename="../../EventsGUI.py" line="394"/>
        <source>No Motion</source>
        <translation>无动作</translation>
    </message>
    <message>
        <location filename="../../EventsGUI.py" line="403"/>
        <source>Activates when there is motion detected</source>
        <translation>当摄像头检测到动作时，运行右边的命令</translation>
    </message>
    <message>
        <location filename="../../EventsGUI.py" line="441"/>
        <source>Object Recognized</source>
        <translation>物体识别</translation>
    </message>
    <message>
        <location filename="../../EventsGUI.py" line="420"/>
        <source>Object &apos;</source>
        <translation>识别&apos;</translation>
    </message>
    <message>
        <location filename="../../EventsGUI.py" line="422"/>
        <source>&apos; Recognized</source>
        <translation>&apos; </translation>
    </message>
    <message>
        <location filename="../../EventsGUI.py" line="431"/>
        <source>Activates when the object </source>
        <translation>当摄像头检测到 </translation>
    </message>
    <message>
        <location filename="../../EventsGUI.py" line="431"/>
        <source> is seen on camera.</source>
        <translation> 时运行右边的命令。</translation>
    </message>
</context>
<context>
    <name>MainWindow</name>
    <message>
        <location filename="../../MainGUI.py" line="76"/>
        <source>uArm Creator Studio</source>
        <translation>uArm创意百宝箱</translation>
    </message>
    <message>
        <location filename="../../MainGUI.py" line="77"/>
        <source>Run</source>
        <translation>运行</translation>
    </message>
    <message>
        <location filename="../../MainGUI.py" line="78"/>
        <source>Devices</source>
        <translation>设备</translation>
    </message>
    <message>
        <location filename="../../MainGUI.py" line="131"/>
        <source>New Task</source>
        <translation>新建任务</translation>
    </message>
    <message>
        <location filename="../../MainGUI.py" line="132"/>
        <source>Save Task</source>
        <translation>保存任务</translation>
    </message>
    <message>
        <location filename="../../MainGUI.py" line="133"/>
        <source>Save Task As</source>
        <translation>另存为任务</translation>
    </message>
    <message>
        <location filename="../../MainGUI.py" line="134"/>
        <source>Load Task</source>
        <translation>导入任务</translation>
    </message>
    <message>
        <location filename="../../MainGUI.py" line="159"/>
        <source>Visit the forum!</source>
        <translation>欢迎访问论坛！</translation>
    </message>
    <message>
        <location filename="../../MainGUI.py" line="160"/>
        <source>Visit our subreddit!</source>
        <translation>欢迎参与 subreddit讨论!</translation>
    </message>
    <message>
        <location filename="../../MainGUI.py" line="171"/>
        <source>Vision Object</source>
        <translation>可识别物体</translation>
    </message>
    <message>
        <location filename="../../MainGUI.py" line="172"/>
        <source>Vision Group</source>
        <translation>可识别物体分组</translation>
    </message>
    <message>
        <location filename="../../MainGUI.py" line="173"/>
        <source>Movement Recording</source>
        <translation>录制新动作</translation>
    </message>
    <message>
        <location filename="../../MainGUI.py" line="174"/>
        <source>Function</source>
        <translation>函数/自定义功能</translation>
    </message>
    <message>
        <location filename="../../MainGUI.py" line="243"/>
        <source>Calibrate</source>
        <translation>校正</translation>
    </message>
    <message>
        <location filename="../../MainGUI.py" line="244"/>
        <source>Resources</source>
        <translation>素材库</translation>
    </message>
    <message>
        <location filename="../../MainGUI.py" line="246"/>
        <source>Run/Pause the command script (Ctrl+R)</source>
        <translation>运行/暂停任务 (Ctrl+R)</translation>
    </message>
    <message>
        <location filename="../../MainGUI.py" line="247"/>
        <source>Open Camera and Robot settings</source>
        <translation>连接摄像头和uArm</translation>
    </message>
    <message>
        <location filename="../../MainGUI.py" line="248"/>
        <source>Open Robot and Camera Calibration Center</source>
        <translation>校正中心（视觉功能 &amp; 运动检测功能）</translation>
    </message>
    <message>
        <location filename="../../MainGUI.py" line="249"/>
        <source>Open Resource Manager</source>
        <translation>进入素材库</translation>
    </message>
    <message>
        <location filename="../../MainGUI.py" line="251"/>
        <source>Ctrl+R</source>
        <translation>Ctrl+R</translation>
    </message>
    <message>
        <location filename="../../MainGUI.py" line="286"/>
        <source>Camera</source>
        <translation>摄像头</translation>
    </message>
    <message>
        <location filename="../../MainGUI.py" line="287"/>
        <source>Console</source>
        <translation>控制台</translation>
    </message>
    <message>
        <location filename="../../MainGUI.py" line="378"/>
        <source>Certain Events and Commands are missing the following requirements to work properly: 

</source>
        <translation>某些事件和命令无法正常运行，请先满足以下条件：</translation>
    </message>
    <message>
        <location filename="../../MainGUI.py" line="379"/>
        <source>
Would you like to continue anyways? Events and commands with errors will not activate.</source>
        <translation>
事件和命令出错，无法运行，你还要继续运行任务吗？</translation>
    </message>
    <message>
        <location filename="../../MainGUI.py" line="776"/>
        <source>Warning</source>
        <translation>警告</translation>
    </message>
    <message>
        <location filename="../../MainGUI.py" line="419"/>
        <source>The script was unable to end.
This may mean the script crashed, or it is taking time finishing.

If you are running Python code inside of this script, make sure you check isExiting() during loops, to exit code quickly when the stop button is pressed.</source>
        <translation>命令无法结束运行。

这意味着命令已经崩溃，或无法马上停止运行。
如果你在命令中运行了 python 代码，请确保 isExiting() 在循环命令中。这可以确保当你按下“停止”后，命令能快速终止。</translation>
    </message>
    <message>
        <location filename="../../MainGUI.py" line="446"/>
        <source>Start</source>
        <translation>开始</translation>
    </message>
    <message>
        <location filename="../../MainGUI.py" line="463"/>
        <source>Communication Errors</source>
        <translation>通信协议错误</translation>
    </message>
    <message>
        <location filename="../../MainGUI.py" line="463"/>
        <source>The following errors have occured communicating with your robot.
Try reconnecting under the Devices menu.

ERROR:
</source>
        <translation>此软件在连接uArm时出错，正在尝试重新连接。

错误信息：
</translation>
    </message>
    <message>
        <location filename="../../MainGUI.py" line="622"/>
        <source>not found!</source>
        <translation type="obsolete">未找到！</translation>
    </message>
    <message>
        <location filename="../../MainGUI.py" line="663"/>
        <source>

 The following error occured: </source>
        <translation>

出现以下错误：</translation>
    </message>
    <message>
        <location filename="../../MainGUI.py" line="130"/>
        <source>File</source>
        <translation>文件</translation>
    </message>
    <message>
        <location filename="../../MainGUI.py" line="158"/>
        <source>Community</source>
        <translation>社区</translation>
    </message>
    <message>
        <location filename="../../MainGUI.py" line="170"/>
        <source>New Resource</source>
        <translation>新建素材</translation>
    </message>
    <message>
        <location filename="../../MainGUI.py" line="195"/>
        <source>Languages</source>
        <translation>语言</translation>
    </message>
    <message>
        <location filename="../../MainGUI.py" line="196"/>
        <source>English</source>
        <translation>英语</translation>
    </message>
    <message>
        <location filename="../../MainGUI.py" line="197"/>
        <source>Chinese</source>
        <translation>中文</translation>
    </message>
    <message>
        <location filename="../../MainGUI.py" line="240"/>
        <source>MainToolbar</source>
        <translation>主工具栏</translation>
    </message>
    <message>
        <location filename="../../MainGUI.py" line="684"/>
        <source>You have unsaved changes. Would you like to save before continuing?</source>
        <translation>你是否要保存刚刚的修改？</translation>
    </message>
    <message>
        <location filename="../../MainGUI.py" line="218"/>
        <source>About</source>
        <translation>关于</translation>
    </message>
    <message>
        <location filename="../../MainGUI.py" line="139"/>
        <source>Version: </source>
        <translation>版本：</translation>
    </message>
    <message>
        <location filename="../../MainGUI.py" line="776"/>
        <source>Language switching need restart to apply, Would you like to continue?</source>
        <translation>切换语言后需要重启软件。你要继续切换吗？</translation>
    </message>
    <message>
        <location filename="../../MainGUI.py" line="216"/>
        <source>Help</source>
        <translation>帮助</translation>
    </message>
    <message>
        <location filename="../../MainGUI.py" line="135"/>
        <source>Open Home Folder</source>
        <translation>打开主目录</translation>
    </message>
    <message>
        <location filename="../../MainGUI.py" line="663"/>
        <source>The program was unable to load the following script:
</source>
        <translation>程序无法加载以下脚本：
</translation>
    </message>
    <message>
        <location filename="../../MainGUI.py" line="189"/>
        <source>Reset Layout</source>
        <translation>重置窗口布局</translation>
    </message>
    <message>
        <location filename="../../MainGUI.py" line="701"/>
        <source>Layout Reset need restart to apply, Would you like to continue?</source>
        <translation>重置布局需要重启，你是否要继续？</translation>
    </message>
    <message>
        <location filename="../../MainGUI.py" line="407"/>
        <source>Stop</source>
        <translation>终止</translation>
    </message>
    <message>
        <location filename="../../MainGUI.py" line="210"/>
        <source>Win A Gift!</source>
        <translation>有奖调查</translation>
    </message>
    <message>
        <location filename="../../MainGUI.py" line="208"/>
        <source>Survey</source>
        <translation type="obsolete">调查</translation>
    </message>
    <message>
        <location filename="../../MainGUI.py" line="217"/>
        <source>Bug Report</source>
        <translation>问题反馈</translation>
    </message>
    <message>
        <location filename="../../MainGUI.py" line="215"/>
        <source>Feedback</source>
        <translation type="obsolete">问题反馈</translation>
    </message>
    <message>
        <location filename="../../MainGUI.py" line="219"/>
        <source>User Manual</source>
        <translation>用户指南</translation>
    </message>
    <message>
        <location filename="../../MainGUI.py" line="188"/>
        <source>Settings</source>
        <translation>设置</translation>
    </message>
    <message>
        <location filename="../../MainGUI.py" line="139"/>
        <source>Protocol Version: </source>
        <translation>通信协议版本号：</translation>
    </message>
</context>
<context>
    <name>ObjectManagerGUI</name>
    <message>
        <location filename="../../ObjectManagerGUI.py" line="1796"/>
        <source>You must input a name to continue</source>
        <translation>请输入名称后再继续下一步</translation>
    </message>
    <message>
        <location filename="../../ObjectManagerGUI.py" line="1811"/>
        <source>You cannot have the following characters in the resource name: </source>
        <translation>素材名称不能包含以下字符：</translation>
    </message>
    <message>
        <location filename="../../ObjectManagerGUI.py" line="1818"/>
        <source>There is already a resource named </source>
        <translation>该名称已存在。</translation>
    </message>
    <message>
        <location filename="../../ObjectManagerGUI.py" line="1819"/>
        <source> If you want to replace it, delete the original and try again.</source>
        <translation> 如果你要替换它，请删除原来的文件后重试。</translation>
    </message>
    <message>
        <location filename="../../ObjectManagerGUI.py" line="1822"/>
        <source>That name is too long.</source>
        <translation>名称过长，再取一个吧。</translation>
    </message>
    <message>
        <location filename="../../ObjectManagerGUI.py" line="1825"/>
        <source>Names cannot end with a space.</source>
        <translation>名称不能以空格结尾。</translation>
    </message>
    <message>
        <location filename="../../ObjectManagerGUI.py" line="74"/>
        <source>New Vision Object</source>
        <translation>新建可识别物体</translation>
    </message>
    <message>
        <location filename="../../ObjectManagerGUI.py" line="76"/>
        <source>New Move Recording</source>
        <translation>录制新动作</translation>
    </message>
    <message>
        <location filename="../../ObjectManagerGUI.py" line="77"/>
        <source>New Function</source>
        <translation>新建自定义功能</translation>
    </message>
    <message>
        <location filename="../../ObjectManagerGUI.py" line="113"/>
        <source>Loaded Objects</source>
        <translation>可用素材</translation>
    </message>
    <message>
        <location filename="../../ObjectManagerGUI.py" line="120"/>
        <source>Selected Resource</source>
        <translation>已选素材</translation>
    </message>
    <message>
        <location filename="../../ObjectManagerGUI.py" line="156"/>
        <source>Resource Manager</source>
        <translation>素材库</translation>
    </message>
    <message>
        <location filename="../../ObjectManagerGUI.py" line="187"/>
        <source>Vision Objects</source>
        <translation>可识别物体</translation>
    </message>
    <message>
        <location filename="../../ObjectManagerGUI.py" line="188"/>
        <source>Vision Groups</source>
        <translation>可识别物体分组</translation>
    </message>
    <message>
        <location filename="../../ObjectManagerGUI.py" line="189"/>
        <source>Movement Recordings</source>
        <translation>已录制的动作</translation>
    </message>
    <message>
        <location filename="../../ObjectManagerGUI.py" line="190"/>
        <source>Functions</source>
        <translation>自定义</translation>
    </message>
    <message>
        <location filename="../../ObjectManagerGUI.py" line="343"/>
        <source>Delete</source>
        <translation>删除</translation>
    </message>
    <message>
        <location filename="../../ObjectManagerGUI.py" line="259"/>
        <source>Add Orientation</source>
        <translation>添加新的识别角度</translation>
    </message>
    <message>
        <location filename="../../ObjectManagerGUI.py" line="358"/>
        <source>Name: 
</source>
        <translation>名称：
</translation>
    </message>
    <message>
        <location filename="../../ObjectManagerGUI.py" line="281"/>
        <source>Detail Points: 
</source>
        <translation>可识别特征总数： 
</translation>
    </message>
    <message>
        <location filename="../../ObjectManagerGUI.py" line="281"/>
        <source>Orientations: 
</source>
        <translation>可识别角度：
</translation>
    </message>
    <message>
        <location filename="../../ObjectManagerGUI.py" line="281"/>
        <source>Belongs To Groups:
</source>
        <translation>所属分组：
</translation>
    </message>
    <message>
        <location filename="../../ObjectManagerGUI.py" line="281"/>
        <source>Image:</source>
        <translation>图像：</translation>
    </message>
    <message>
        <location filename="../../ObjectManagerGUI.py" line="296"/>
        <source>Edit Group</source>
        <translation>编辑分组</translation>
    </message>
    <message>
        <location filename="../../ObjectManagerGUI.py" line="305"/>
        <source>Group Members: 
</source>
        <translation>此分组包括：
</translation>
    </message>
    <message>
        <location filename="../../ObjectManagerGUI.py" line="318"/>
        <source>Edit Recording</source>
        <translation>编辑已录制动作</translation>
    </message>
    <message>
        <location filename="../../ObjectManagerGUI.py" line="329"/>
        <source>Move Count: 
</source>
        <translation>运动数据总量：</translation>
    </message>
    <message>
        <location filename="../../ObjectManagerGUI.py" line="358"/>
        <source>Length: 
</source>
        <translation>录制时长/命令总数：</translation>
    </message>
    <message>
        <location filename="../../ObjectManagerGUI.py" line="329"/>
        <source>Moves/Second:
</source>
        <translation>运动数据量/秒：</translation>
    </message>
    <message>
        <location filename="../../ObjectManagerGUI.py" line="344"/>
        <source>Edit Function</source>
        <translation>编辑自定义功能</translation>
    </message>
    <message>
        <location filename="../../ObjectManagerGUI.py" line="358"/>
        <source>Description: 
</source>
        <translation>描述：</translation>
    </message>
    <message>
        <location filename="../../ObjectManagerGUI.py" line="358"/>
        <source> Commands

</source>
        <translation>命令</translation>
    </message>
    <message>
        <location filename="../../ObjectManagerGUI.py" line="358"/>
        <source>Arguments:
</source>
        <translation>变量：</translation>
    </message>
    <message>
        <location filename="../../ObjectManagerGUI.py" line="392"/>
        <source>Warning</source>
        <translation>警告</translation>
    </message>
    <message>
        <location filename="../../ObjectManagerGUI.py" line="392"/>
        <source>Deleting this object will delete it permanently.
</source>
        <translation>删除后不可撤消。
</translation>
    </message>
    <message>
        <location filename="../../ObjectManagerGUI.py" line="392"/>
        <source>Do you want to continue?</source>
        <translation>你是否要继续？</translation>
    </message>
    <message>
        <location filename="../../ObjectManagerGUI.py" line="1073"/>
        <source>Apply</source>
        <translation>应用</translation>
    </message>
    <message>
        <location filename="../../ObjectManagerGUI.py" line="497"/>
        <source>Group Name: </source>
        <translation>分组名称：</translation>
    </message>
    <message>
        <location filename="../../ObjectManagerGUI.py" line="1107"/>
        <source>Cancel</source>
        <translation>取消</translation>
    </message>
    <message>
        <location filename="../../ObjectManagerGUI.py" line="537"/>
        <source>Add Objects to Group</source>
        <translation>可识别物体分组</translation>
    </message>
    <message>
        <location filename="../../ObjectManagerGUI.py" line="569"/>
        <source>You must select at least one object</source>
        <translation>你至少要选择一个物体</translation>
    </message>
    <message>
        <location filename="../../ObjectManagerGUI.py" line="775"/>
        <source>Record</source>
        <translation>录制</translation>
    </message>
    <message>
        <location filename="../../ObjectManagerGUI.py" line="632"/>
        <source>A robot must be connected to do movement recording.</source>
        <translation>请先连接uArm，再录制新动作。</translation>
    </message>
    <message>
        <location filename="../../ObjectManagerGUI.py" line="633"/>
        <source>Error</source>
        <translation>错误</translation>
    </message>
    <message>
        <location filename="../../ObjectManagerGUI.py" line="652"/>
        <source>Time</source>
        <translation>时间</translation>
    </message>
    <message>
        <location filename="../../ObjectManagerGUI.py" line="652"/>
        <source>Servo Angles</source>
        <translation>电机角度</translation>
    </message>
    <message>
        <location filename="../../ObjectManagerGUI.py" line="652"/>
        <source>Gripper Action</source>
        <translation>末端动作</translation>
    </message>
    <message>
        <location filename="../../ObjectManagerGUI.py" line="658"/>
        <source>Recording Name: </source>
        <translation>动作名称： </translation>
    </message>
    <message>
        <location filename="../../ObjectManagerGUI.py" line="659"/>
        <source>Recorded Path</source>
        <translation>已录制的运动轨迹</translation>
    </message>
    <message>
        <location filename="../../ObjectManagerGUI.py" line="660"/>
        <source>Press &apos;Record&apos; to start recording robot movements.
</source>
        <translation>点击&apos;录制&apos;，开始录制新的uArm动作。
</translation>
    </message>
    <message>
        <location filename="../../ObjectManagerGUI.py" line="660"/>
        <source>While recording, press the robots suction cup to activate the pump.
</source>
        <translation>开始录制时，按压uArm末端吸盘，uArm即开始吸取，再按一下，uArm停止吸取。</translation>
    </message>
    <message>
        <location filename="../../ObjectManagerGUI.py" line="660"/>
        <source>When you press Apply, areas of no movement at the start and end
</source>
        <translation>点击“应用”后，录制过程中机械臂静止的部分
</translation>
    </message>
    <message>
        <location filename="../../ObjectManagerGUI.py" line="660"/>
        <source>will be trimmed out.</source>
        <translation>将会自动被去除。</translation>
    </message>
    <message>
        <location filename="../../ObjectManagerGUI.py" line="723"/>
        <source>Create a Movement Recording</source>
        <translation>录制新的uArm动作</translation>
    </message>
    <message>
        <location filename="../../ObjectManagerGUI.py" line="777"/>
        <source>Continue Recording</source>
        <translation>继续录制uArm动作</translation>
    </message>
    <message>
        <location filename="../../ObjectManagerGUI.py" line="791"/>
        <source>Stop Recording</source>
        <translation>停止录制</translation>
    </message>
    <message>
        <location filename="../../ObjectManagerGUI.py" line="961"/>
        <source>Recording must be longer than 20 points of data</source>
        <translation>请控制好录制的动作幅度，
请避免动作幅度过小导致无法录制，或幅度过大导致uArm损坏。</translation>
    </message>
    <message>
        <location filename="../../ObjectManagerGUI.py" line="1008"/>
        <source>Add Argument</source>
        <translation>添加变量</translation>
    </message>
    <message>
        <location filename="../../ObjectManagerGUI.py" line="1008"/>
        <source>Variable Name: </source>
        <translation>变量名称：</translation>
    </message>
    <message>
        <location filename="../../ObjectManagerGUI.py" line="1021"/>
        <source>Invalid Variable Name</source>
        <translation>无效变量名称</translation>
    </message>
    <message>
        <location filename="../../ObjectManagerGUI.py" line="1021"/>
        <source>The argument must be a valid python variable. This means no numbers </source>
        <translation>变量名称只能由字母和数字组成，</translation>
    </message>
    <message>
        <location filename="../../ObjectManagerGUI.py" line="1021"/>
        <source>in the beginning, no spaces, and only numbers and letters</source>
        <translation>且不能以数字开头，不能含有空格。</translation>
    </message>
    <message>
        <location filename="../../ObjectManagerGUI.py" line="1103"/>
        <source>Function Name </source>
        <translation>功能名称 </translation>
    </message>
    <message>
        <location filename="../../ObjectManagerGUI.py" line="1104"/>
        <source>Function Description </source>
        <translation>功能描述 </translation>
    </message>
    <message>
        <location filename="../../ObjectManagerGUI.py" line="1105"/>
        <source>Arguments (optional)</source>
        <translation>变量 (选填)</translation>
    </message>
    <message>
        <location filename="../../ObjectManagerGUI.py" line="1106"/>
        <source>Drag commands into the list to create a function</source>
        <translation>把命令拖拽到列表中，即可新建自定义功能</translation>
    </message>
    <message>
        <location filename="../../ObjectManagerGUI.py" line="1174"/>
        <source>Create a Function</source>
        <translation>新建函数/自定义功能</translation>
    </message>
    <message>
        <location filename="../../ObjectManagerGUI.py" line="1241"/>
        <source>Object Wizard</source>
        <translation> uArm“开眼”向导</translation>
    </message>
    <message>
        <location filename="../../ObjectManagerGUI.py" line="1251"/>
        <source>A camera must be connected to add new objects</source>
        <translation>请先连接摄像头，再添加新的可识别物体</translation>
    </message>
    <message>
        <location filename="../../ObjectManagerGUI.py" line="1316"/>
        <source>Welcome to the Object Wizard!
</source>
        <translation>欢迎添加新的可识别物体！
</translation>
    </message>
    <message>
        <location filename="../../ObjectManagerGUI.py" line="1317"/>
        <source>This will walk you through teaching the software how to recognize a new object.</source>
        <translation>请根据引导完成以下步骤，让uArm“看见”一个新物体。</translation>
    </message>
    <message>
        <location filename="../../ObjectManagerGUI.py" line="1318"/>
        <source>

Step 1: Naming</source>
        <translation>

第1步：命名</translation>
    </message>
    <message>
        <location filename="../../ObjectManagerGUI.py" line="1319"/>
        <source>Please enter a unique name for this object.</source>
        <translation>给你的物体取个名字吧！</translation>
    </message>
    <message>
        <location filename="../../ObjectManagerGUI.py" line="1417"/>
        <source>

Step 2: Select the Object</source>
        <translation type="obsolete">

第2步：选择物体</translation>
    </message>
    <message>
        <location filename="../../ObjectManagerGUI.py" line="1418"/>
        <source>Please place the object you want to recognize ON THE TABLES SURFACE, in the middle of the screen.


                Make sure the background is consistent and there is nothing on the screen except the object. The
                
work area should be well lit, but not cause too much glare on the object if it&apos;s shiny. The video
                
should be focused, and the object in the orientation that it will be recognized in. 


                When ready, Click the mouse on the corner of the object, drag it tightly over the object, then
            
release the mouse button.</source>
        <translation type="obsolete">1. 请将你的物体置于平面上，并确保：

1）物体位于摄像头视野的中心；
2）物体的空间背景干净、无杂物；
3）光线充足，但不会导致物体反光；

2. 用鼠标拖拽选取物体（如右边GIF所示）。</translation>
    </message>
    <message>
        <location filename="../../ObjectManagerGUI.py" line="1421"/>
        <source>

Step 3: Verify</source>
        <translation>

第3步：预览识别效果</translation>
    </message>
    <message>
        <location filename="../../ObjectManagerGUI.py" line="1503"/>
        <source>-test text-</source>
        <translation>-测试 文本-</translation>
    </message>
    <message>
        <location filename="../../ObjectManagerGUI.py" line="1539"/>
        <source>Your selected object needs more detail to be tracked</source>
        <translation>为了更好地识别你所选取的物体，请在物体上增加更多细节特征</translation>
    </message>
    <message>
        <location filename="../../ObjectManagerGUI.py" line="1556"/>
        <source>Good job, you have selected an object. Try moving the object around to see how accurate the
            
tracking is. If it&apos;s not good enough, click &apos;Try Again&apos;&apos; on the bottom right of the camera to
            
reselect the object.


            Your selected object has </source>
        <translation>你已选取想要识别的物体。
现在，试着移动该物体，看看摄像头是否能实时追踪它的位置。如果追踪效果不太好，请重新选取物体。你所选取的物体共有</translation>
    </message>
    <message>
        <location filename="../../ObjectManagerGUI.py" line="1560"/>
        <source>points to describe it.
            The more detail on the object, the more points
            
will be found, and the better the tracking will be. If you are having trouble tracking, try adding
            
detail to the object by drawing on it or putting a sticker on it. 

            </source>
        <translation> 个可识别特征。

小提示：
细节特征越多，识别效果越好。
如果摄像头无法很好地实时追踪你的物体，请再物体上画上更多细节特征，或贴上二维码/贴纸。
</translation>
    </message>
    <message>
        <location filename="../../ObjectManagerGUI.py" line="1570"/>
        <source>Your selected object has only </source>
        <translation>摄像头只识别到 </translation>
    </message>
    <message>
        <location filename="../../ObjectManagerGUI.py" line="1570"/>
        <source> points to describe it. It is not very</source>
        <translation>个细节特征。</translation>
    </message>
    <message>
        <location filename="../../ObjectManagerGUI.py" line="1570"/>
        <source> detailed, or is too small. Try adding more detail by drawing on it, or adding a </source>
        <translation>此物体特征不够明显，或太小。识别/实时追踪效果不佳。
请增加更多细节特征或</translation>
    </message>
    <message>
        <location filename="../../ObjectManagerGUI.py" line="1570"/>
        <source>sticker to it. Tracking may not be very accurate.</source>
        <translation>给物体贴上二维码/贴纸。</translation>
    </message>
    <message>
        <location filename="../../ObjectManagerGUI.py" line="1574"/>
        <source>Tracking </source>
        <translation>识别到 </translation>
    </message>
    <message>
        <location filename="../../ObjectManagerGUI.py" line="1603"/>
        <source>

Step 4: Measure Height</source>
        <translation>

第4步：测量物体高度</translation>
    </message>
    <message>
        <location filename="../../ObjectManagerGUI.py" line="1604"/>
        <source>Please enter the height of the object in centimeters. </source>
        <translation>请输入物体的高度(cm)。</translation>
    </message>
    <message>
        <location filename="../../ObjectManagerGUI.py" line="1604"/>
        <source>
If the object is very thin, like paper, enter 0.</source>
        <translation>
如果物体非常薄（如纸张），请输入0。</translation>
    </message>
    <message>
        <location filename="../../ObjectManagerGUI.py" line="1604"/>
        <source>
If the object is not flat on the top, measure the height to the part of the </source>
        <translation>如果物体不是平整的，请测量uArm可吸起部分</translation>
    </message>
    <message>
        <location filename="../../ObjectManagerGUI.py" line="1604"/>
        <source>object that the robot will be grasping.</source>
        <translation>的高度。</translation>
    </message>
    <message>
        <location filename="../../ObjectManagerGUI.py" line="1609"/>
        <source> centimeters</source>
        <translation>厘米</translation>
    </message>
    <message>
        <location filename="../../ObjectManagerGUI.py" line="1647"/>
        <source>You must input a real number.</source>
        <translation>请输入一个数字。</translation>
    </message>
    <message>
        <location filename="../../ObjectManagerGUI.py" line="1651"/>
        <source>Height must be a number greater than or equal to 0.</source>
        <translation>高度必须大于或等于 0。</translation>
    </message>
    <message>
        <location filename="../../ObjectManagerGUI.py" line="1694"/>
        <source>You&apos;re almost done!

</source>
        <translation>最后一步！

</translation>
    </message>
    <message>
        <location filename="../../ObjectManagerGUI.py" line="1695"/>
        <source>Now that you have selected your object, please drag the mouse over THE ENTIRE AREA OF THE OBJECT 
</source>
        <translation>为方便uArm能轻松捡起此物体，
请用鼠标在拖拽出此物体可被拾取的全部范围。
</translation>
    </message>
    <message>
        <location filename="../../ObjectManagerGUI.py" line="1696"/>
        <source>
that is smooth, flat, and able to be picked up by the robot&apos;s suction cup. 

</source>
        <translation>
小提示：
1）可拾取范围不宜过小，请选取全部可被拾取的范围；
2）为了让吸盘能顺利吸起物体，可拾取范围内必须是平滑、不漏气（无孔）的表面。
</translation>
    </message>
    <message>
        <location filename="../../ObjectManagerGUI.py" line="1697"/>
        <source>
This information will be used in any commands that require the robot to pick up the object. If you</source>
        <translation>
如果你不打算让uArm捡起此物体，</translation>
    </message>
    <message>
        <location filename="../../ObjectManagerGUI.py" line="1698"/>
        <source>
do not intend to use those functions, then just select an area around the center of the object.

</source>
        <translation>直接选取物体中心区域即可。
</translation>
    </message>
    <message>
        <location filename="../../ObjectManagerGUI.py" line="1700"/>
        <source>Step 5: Select the Pickup Area</source>
        <translation>第5步：设置物体被拾取的方式</translation>
    </message>
    <message>
        <location filename="../../ObjectManagerGUI.py" line="1712"/>
        <source>Could not find example gif</source>
        <translation>找不到示例 gif</translation>
    </message>
    <message>
        <location filename="../../ObjectManagerGUI.py" line="1760"/>
        <source>Congratulations, you&apos;ve created a new object! </source>
        <translation>恭喜，你让uArm又“看见”了一个物体！</translation>
    </message>
    <message>
        <location filename="../../ObjectManagerGUI.py" line="1760"/>
        <source>
This will now be saved in a seperate file, and can be used in any project.</source>
        <translation>
这已被保存成独立文件，你可随时调用。</translation>
    </message>
    <message>
        <location filename="../../ObjectManagerGUI.py" line="75"/>
        <source>New Vision Group</source>
        <translation>新建可识别物体分组</translation>
    </message>
    <message>
        <location filename="../../ObjectManagerGUI.py" line="1412"/>
        <source>
Step 2: Select the Object</source>
        <translation>
步骤 2：选择一个要识别的物体</translation>
    </message>
    <message>
        <location filename="../../ObjectManagerGUI.py" line="1491"/>
        <source>Step 2: Select the Object</source>
        <translation>步骤 2：选择一个要识别的物体</translation>
    </message>
    <message>
        <location filename="../../ObjectManagerGUI.py" line="1502"/>
        <source>Step 3: Verify</source>
        <translation>步骤 3：验证</translation>
    </message>
    <message>
        <location filename="../../ObjectManagerGUI.py" line="1413"/>
        <source>1. Please place the object you want to recognize ON THE TABLES SURFACE, in the middle of the screen.
1）Make sure the background is consistent and there is nothing on the screen except the object.
2）The work area should be well lit, but not cause too much glare on the object if it&apos;s shiny.

2. When ready, Click the mouse on the corner of the object, drag it tightly over the object, then release the mouse button.</source>
        <translation>1. 请将你的物体置于平面上，并确保：

1）物体位于摄像头视野的中心；
2）物体的空间背景干净、无杂物；
3）光线充足，但不会导致物体反光；

2. 用鼠标拖拽选取物体。</translation>
    </message>
</context>
<context>
    <name>ScriptWidget</name>
    <message>
        <location filename="../../CommonGUI.py" line="374"/>
        <source>Show Documentation</source>
        <translation>Python编程指引</translation>
    </message>
    <message>
        <location filename="../../CommonGUI.py" line="379"/>
        <source>Show Code</source>
        <translation>显示代码</translation>
    </message>
</context>
</TS>
