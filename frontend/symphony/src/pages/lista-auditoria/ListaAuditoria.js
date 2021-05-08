import React from 'react'
import DataTable from '../../components/datatable/datatable'
import { POST_LIST_AUDITORIA } from '../../system/constants'
import {Field} from 'formik'

import '../../styles/scss/pages/basic/forms.scss'


const ListaAuditoria = () => {
    var configuraciones = {
        page_size: 50,
        url: POST_LIST_AUDITORIA,
        form: <>
                <div className="field-group">
                    <Field name="api_name" className="field" placeholder="Nome da api"/>
                </div>
            </>
    }

    return <DataTable configurations={ configuraciones}/>
}

export default ListaAuditoria