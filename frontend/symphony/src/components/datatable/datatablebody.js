import React from 'react'
import { Link } from 'react-router-dom'
import { Button } from 'react-bootstrap';

export default function DataTableBody(parameters) {
    return <>
        <tbody className="body">
            {parameters.data.body.map(
                (line) =>
                    <tr>
                        {console.log(line)}
                        {
                            parameters.configurations.actions.map(
                                (action) =>
                                    <td className="row">
                                        <Button variant="outline-dark" to={`/${action.path}?key=${line.key}`}>
                                            {action.icon}
                                            <span>{action.title}</span>
                                        </Button>
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