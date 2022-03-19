import React from 'react'


const ProjectItem = ({project}) => {
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
const ProjectList = ({projects}) => {
    return(
        <table border={1} bgcolor={'LightSteelBlue'}>
            <th>
                Project name
            </th>
            <th>
                Project URL
            </th>
            {projects.map((project) => <ProjectItem project={project}/>)}
        </table>
    )
}

export default ProjectList