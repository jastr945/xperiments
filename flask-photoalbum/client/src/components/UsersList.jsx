import React from 'react';

const Timestamp = require('react-timestamp');

const UsersList = (props) => {
  return (
    <div>
      {
        props.users.map((user) => {
          return (
            <h4
              key={user.id}
              className="well"
            >{user.username} - {user.email} - <Timestamp time={user.created_at} format='full' /> - <Timestamp time={user.created_at} format='ago' includeDay={true} precision={2} autoUpdate={60} />
            </h4>
          )
        })
      }
    </div>
  )
};

export default UsersList;
