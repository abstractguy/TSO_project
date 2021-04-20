#ifndef _UARMCONTROLLER_HH_
#define _UARMCONTROLLER_HH_

#include "gazebo/gazebo.hh"
#include "gazebo/physics/physics.hh"
#include "gazebo/transport/TransportTypes.hh"
#include <gazebo/transport/transport.hh>
#include <gazebo/msgs/msgs.hh>
#include "new_position.pb.h"
#include <iostream>

#define NUM_JOINTS 3
typedef const boost::shared_ptr<const uarm_msgs::msgs::NewPosition> NewPosition;

namespace gazebo
{
class UarmController : public ModelPlugin
{
public:
  UarmController();

public:
  virtual void Load(physics::ModelPtr _model, sdf::ElementPtr _sdf);

/// \brief Callback method for updateConnection, is called in every world update.
/// In this callback the PID-Controller calculate the effort for the three joints.
/// After the calculation the values will be applied.
public: void OnUpdate();

/// \brief Callback method for the joint position subscriber.
/// In this method the values from the message will be saved into jointPosition.
/// The values will be applied in the next OnUpdate() call.
private: void MoveCallback(NewPosition &_msg);

/// \brief This method initializes the plugin, but we do nothing in here.
private: virtual void Init();

// transport node
private: transport::NodePtr node;

// connection pointer to update the world
private: event::ConnectionPtr updateConnection;

// model pointer to get access to the joints
private: physics::ModelPtr model;

// joint pointer with all joints we want to move
private: gazebo::transport::SubscriberPtr sub;

// Jointpointers for all the joints
private: physics::JointPtr joints[NUM_JOINTS];

// pid controller for the joints
private: common::PID jointPIDs[NUM_JOINTS];

// joint position for all needed joints
private: double jointPositions[NUM_JOINTS];

// joint velocities for all needed joints
private: double jointVelocities[NUM_JOINTS];

// joint efforts for all needed joints
private: double jointMaxEfforts[NUM_JOINTS];

// time before we update the joint values
private: common::Time prevUpdateTime;

};
GZ_REGISTER_MODEL_PLUGIN(UarmController)
}
#endif
