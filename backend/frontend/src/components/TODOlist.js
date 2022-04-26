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
            <td>
                <button onClick={() => deleteToDo(project.id)} type='button'>Delete</button>
            </td>

        </tr>
    )
}
const TODOList = ({TODOs, deleteToDo}) => {
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
            <th>

            </th>
            {TODOs.map((TODO) => <TODOItem TODO={TODO}/>)}
            {ToDos.map((TODO) => <TODOItem TODO={TODO} deleteToDo={deleteToDo}/>)}
        </table>
    )
}

export default TODOList