import React from 'react'
import {Link} from "react-router-dom";


const UserItem = ({user}) => {
    return(
        <tr>
            <td>
                <Link to={`users/${user.id}`}>{user.user_name}</Link>
            </td>
            <td>
                {user.first_name}
            </td>
            <td>
                {user.last_name}
            </td>
            <td>
                {user.birthday_year}
            </td>
            <td>
                {user.email}
            </td>
        </tr>
    )
}
const UserList = ({users}) => {
    return(
        <table border={1} bgcolor={'LightSteelBlue'}>
            <th>
                User name
            </th>
            <th>
                First name
            </th>
            <th>
                Last name
            </th>
            <th>
                Date of birth
            </th>
            <th>
                E-mail addr
            </th>
            {users.map((user) => <UserItem user={user}/>)}
        </table>
    )
}

export default UserList
