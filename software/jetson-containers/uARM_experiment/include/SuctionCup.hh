#ifndef _SuctionCup_HH_
#define _SuctionCup_HH_

#include "gazebo/gazebo.hh"
#include "gazebo/physics/physics.hh"
#include "gazebo/transport/TransportTypes.hh"
#include <gazebo/transport/transport.hh>
#include <gazebo/msgs/msgs.hh>
#include "suction_cup_contact.pb.h"
#include "new_position.pb.h"

typedef const boost::shared_ptr<const uarm_msgs::msgs::SuctionCupContact> SuctionCupContact;
typedef const boost::shared_ptr<const uarm_msgs::msgs::NewPosition> NewPosition;

namespace gazebo {

/// \class SuctionCup suction_cup.hh
/// \brief Class to control the suction cup
///
/// This class controls the suctioncup at the endeffector
/// of the uarm. There are two subscribers. The sub_con
/// subscriber listens to the ContactPlugin and saves the
/// model and link of the object that is in contact with
/// suction cup. The sub_suck creates a joint between the
/// sucktion cup and the object when called or destroys
/// the joint.

class SuctionCup : public ModelPlugin
{
/// \brief modelptr and linkptr are stored, subscribers are started
public: virtual void Load(physics::ModelPtr _model, sdf::ElementPtr _sdf);

/// \brief nothing happens here
public: void OnUpdate();

/// \brief nothing happens here
private: virtual void Init();

/// \brief callbackmethod for new contacts
private: void ContactCallback(SuctionCupContact &_msg);

/// \brief callbackmethod for new attaching or detaching
private: void SuckCallback(NewPosition &_msg);

// connection pointer to update the world
private: event::ConnectionPtr updateConnection;

// model pointer to get acces to the model
private: physics::ModelPtr model;

// model pointer to get acces to the link
private: physics::LinkPtr link;

// transport node
private: transport::NodePtr node;

// subscriber for contacts
private: gazebo::transport::SubscriberPtr sub_con;

// subscriber for attaching and detaching
private: gazebo::transport::SubscriberPtr sub_suck;

// linkname of the object to attach
private: std::string link_name;

// modelname of the object to attach
private: std::string model_name;

// joint that will be established between the two objects
private: physics::JointPtr _joint;

// variable to check if there is an joint attached
private: bool joint_created;
};
GZ_REGISTER_MODEL_PLUGIN(SuctionCup)
}
#endif
