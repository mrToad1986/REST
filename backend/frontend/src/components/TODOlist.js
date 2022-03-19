import React from 'react'


const TODOItem = ({TODO}) => {
    return(
        <tr>
            <td>
                {TODO.project}
            </td>
            <td>
                {TODO.created_at}
            </td>
            <td>
                {TODO.is_active}
            </td>

        </tr>
    )
}
const TODOList = ({TODOs}) => {
    return(
        <table border={1} bgcolor={'LightSteelBlue'}>
            <th>
                Description
            </th>
            <th>
                Date
            </th>
            <th>
                Status
            </th>

            {TODOs.map((todo) => <TODOItem todo={todo}/>)}
        </table>
    )
}

export default TODOList