import React from 'react'
import DataTable from '../../components/datatable/datatable'
import { POST_LIST_ERROS } from '../../system/constants'
import { Field } from 'formik'
import * as FaIcons from 'react-icons/fa'

import '../../styles/scss/pages/basic/forms.scss'

const ListaErros = () => {
    var configuraciones = {
        page_size: 5,
        url: POST_LIST_ERROS,
        form: <>
                <div className="field-group">
                    <Field name="error_message" className="field" placeholder="Mensagem de erro"/>
                </div>
            </>,
        actions: [
            {
                path: 'log-details',
                icon: <FaIcons.FaSearchPlus />,
                color: 'green'
            }
        ]
    }

    return <DataTable configurations={ configuraciones}/>
}

export default ListaErros