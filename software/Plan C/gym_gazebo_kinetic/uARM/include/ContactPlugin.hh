#ifndef _GAZEBO_CONTACT_PLUGIN_HH_
#define _GAZEBO_CONTACT_PLUGIN_HH_

#include <string>

#include <gazebo/gazebo.hh>
#include <gazebo/sensors/sensors.hh>
#include <gazebo/transport/transport.hh>
#include <gazebo/msgs/msgs.hh>
#include "suction_cup_contact.pb.h"

/// Some parts of the code are copied from here:
/// http://gazebosim.org/tutorials/?tut=contact_sensor
namespace gazebo
{
/// \brief Class to check for Contacts with the suction cup
///
/// Every time the OnUpdate() method is called, all the contacts
/// are evaluated. If there is a contact between the suction cup
/// and an other object in the world, the modelname and linkname
/// is send to the suction cup controller.
class ContactPlugin : public SensorPlugin
{
/// \brief Constructor.
public: ContactPlugin();

/// \brief Destructor.
public: virtual ~ContactPlugin();

/// \brief Load the sensor plugin.
/// \param[in] _sensor Pointer to the sensor that loaded this plugin.
/// \param[in] _sdf SDF element that describes the plugin.
public: virtual void Load(sensors::SensorPtr _sensor, sdf::ElementPtr _sdf);

/// \brief Callback that recieves the contact sensor's update signal.
private: virtual void OnUpdate();

/// \brief Pointer to the contact sensor
private: sensors::ContactSensorPtr parentSensor;

/// \brief Connection that maintains a link between the contact sensor's
/// updated signal and the OnUpdate callback.
private: event::ConnectionPtr updateConnection;

/// publisher for the contacts
private: gazebo::transport::PublisherPtr pub;

/// method to send the model's and link's names
public: void send_message(const char *contact_name);
};
}
#endif
