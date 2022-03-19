import {useParams} from 'react-router-dom'


const UserProjectItem = ({project}) => {
    return(
        <tr>
            <td>
                {project.name}
            </td>
            <td>
                {project.ref}
            </td>
        </tr>
    )
}
const UserProjectList = ({projects}) => {
    var {id} = useParams()
    var filteredProjects = projects.filter((project) => project.users.include(parseInt(id)))
    return(
        <table border={1} bgcolor={'LightSteelBlue'}>
            <th>
                Project name
            </th>
            <th>
                Project URL
            </th>
            {projects.map((project) => <UserProjectItem project={project}/>)}
        </table>
    )
}

export default UserProjectList