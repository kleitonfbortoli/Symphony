import React from 'react'
import { Link } from 'react-router-dom'

export default function DataTableBody(parameters) {
    return <>
        <tbody className="body">
            { console.log(parameters.configurations.body)}
            {parameters.data.body.map(
                (line) =>
                    <tr>
                        {
                            parameters.configurations.actions.map(
                                (action) =>
                                    <td className="row">
                                        <Link to={`/${action.path}?key=${line.key}${action.parameters ?? ''}`} style={{color:action.color}}>
                                            {action.icon}
                                            <span>{action.title}</span>
                                        </Link>
                                    </td>
                            )
                        }
                        {
                            line.data.map(
                                (value) => <td className="row">{value}</td>
                            )
                        }
                    </tr>
            )}
        </tbody>
    </>
}