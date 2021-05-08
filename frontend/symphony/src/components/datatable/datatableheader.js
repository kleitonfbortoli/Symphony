import React from 'react'

export default function DataTableHeader(parameters) {
    
    return <>
        <thead className="header">
            <tr>
                {
                    parameters.configurations.actions.map(
                        () => <th className="row"><imput type="button" onClick/></th>
                    )
                }
                {
                    parameters.data.header.map(
                        value => <th className="row"><b>{value}</b></th>
                    )
                }
            </tr>
        </thead>
    </>
}