import React from 'react'

export default function DataTableNavigation(parameters) {
    var value = []
    var qtd_abas = Math.ceil(parameters.data.count_results / parameters.configurations.page_size);

    for (let index = 1; index <= qtd_abas; index++) {
        value.push(index);
    }

    let colspan = parameters.data.header.length + parameters.configurations.actions.length

    return <>
        <tfoot className="footer">
            <tr>
                <td className="row" colSpan={colspan}>{value.map((index) => <button type='button' className={ index == parameters.page_number ? 'index selected' : 'index'} onClick={parameters.change_function} value={index}>{index}</button>)}</td>
            </tr>
        </tfoot>
    </>
}