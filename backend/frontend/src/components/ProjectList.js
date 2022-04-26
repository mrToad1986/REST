import React from 'react'
import {Link} from 'react-router-dom'


const ProjectItem = ({project}) => {
    return (
        <tr>
            <td>
                {project.name}
            </td>
            <td>
                {project.ref}
            </td>
            <td>
                <button onClick={() => deleteProject(project.id)} type='button'>Delete</button>
            </td>
        </tr>
    )
}
const ProjectList = ({projects, deleteProject}) => {
    return (
        <div>
            <table border={1} bgcolor={'LightSteelBlue'}>
                <th>
                    Project name
                </th>
                <th>
                    Project URL
                </th>
                <th>

                </th>
                {projects.map((project) => <ProjectItem project={project}/>)}
                {projects.map((item) => <ProjectItem project={project} deleteProject={deleteProject}/>)}
            </table>
            <Link to='project/create'>Add project</Link>
        </div>
    )
}

export default ProjectList