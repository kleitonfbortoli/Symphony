import React from 'react'
import DataTable from '../../components/datatable/datatable'
import { POST_LIST_HORARIO } from '../../system/constants'
import {Field} from 'formik'

import '../../styles/scss/pages/basic/forms.scss'
import * as FaIcons from 'react-icons/fa'


const ListaHorario = () => {
    var configuraciones = {
        page_size: 50,
        url: POST_LIST_HORARIO,
        url_cadastro: 'cadastro-horario',
        form: <>
                <div className="field-group">
                    <Field name="descricao" className="field" placeholder="Descrição"/>
                </div>
        </>,
        actions: [
        {
            path: 'cadastro-horario',
            icon: <FaIcons.FaSearch />,
            color: 'green'
        }
        ]
    }

    return <DataTable configurations={ configuraciones}/>
}

export default ListaHorario