import React from 'react'
import DataTable from '../../components/datatable/datatable'
import { POST_LIST_MODULO } from '../../system/constants'
import {Field} from 'formik'

import '../../styles/scss/pages/basic/forms.scss'
import * as FaIcons from 'react-icons/fa'


const ListaModulo = () => {
    var configuraciones = {
        page_size: 50,
        url: POST_LIST_MODULO,
        form: <>
                <div className="field-group">
                    <Field name="descricao" className="field" placeholder="Descrição"/>
                </div>
        </>,
        actions: [
        {
            path: 'modulo-details',
            icon: <FaIcons.FaSearch />,
            // label: 'action teste',
            parameters: '&teste=a'
        }
        ]
    }

    return <DataTable configurations={ configuraciones}/>
}

export default ListaModulo