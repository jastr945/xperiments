import React from 'react';

const UsersList = (props) => {
  return (
    <div>
      {
        props.users.map((user) => {
          return (
            <h4
              key={user.id}
              className="well"
            >{user.username} - {user.email} - {user.created_at}
            </h4>
          )
        })
      }
    </div>
  )
};

export default UsersList;
