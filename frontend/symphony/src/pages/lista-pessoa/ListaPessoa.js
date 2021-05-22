import React from 'react'
import DataTable from '../../components/datatable/datatable'
import { POST_LIST_PESSOA } from '../../system/constants'
import {Field} from 'formik'

import '../../styles/scss/pages/basic/forms.scss'
import * as FaIcons from 'react-icons/fa'


const ListaPessoa = () => {
    var configuraciones = {
        page_size: 50,
        url: POST_LIST_PESSOA,
        form: <>
                <div className="field-group">
                    <Field name="name" className="field" placeholder="Nome"/>
                </div>
        </>,
        actions: [
        {
            path: 'pessoa-details',
            icon: <FaIcons.FaSearch />,
            // label: 'action teste',
            parameters: '&teste=a'
        }
        ]
    }

    return <DataTable configurations={ configuraciones}/>
}

export default ListaPessoa