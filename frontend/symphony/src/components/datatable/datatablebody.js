import React from 'react'
import { Link } from 'react-router-dom'

export default function DataTableBody(parameters) {

    if (typeof parameters.configurations.actions === 'undefined')
    {
        parameters.configurations.actions = [];
    }

    return <>
        <tbody className="body">
            {parameters.data.body.map(
                (line) =>
                    <tr>
                        {
                            parameters.configurations.actions.map(
                                (action) => {
                                    if (action.path)
                                    {
                                        return <td className="row icon">
                                            <Link to={`/${action.path}?key=${line.key}${action.parameters ?? ''}`} style={{ color: action.color }}>
                                                {action.icon}
                                                <span>{action.title}</span>
                                            </Link>
                                        </td>
                                    }
                                    else
                                    {
                                        return <td className="row icon"><span className="action-button" onClick={() =>  action.click(line.key)} style={{ color: action.color }}>{action.icon}</span></td>
                                    }
                                }
                                    
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