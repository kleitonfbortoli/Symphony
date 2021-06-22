import React from 'react'
import DataTable from '../../components/datatable/datatable'
import { POST_LIST_TURMA } from '../../system/constants'
import { Message } from '../../system/message'
import {Field} from 'formik'

import '../../styles/scss/pages/basic/forms.scss'
import * as FaIcons from 'react-icons/fa'
import * as BiIcons from 'react-icons/bi'


const ListaTurma = () => {
    var configuraciones = {
        page_size: 50,
        url: POST_LIST_TURMA,
        url_cadastro: 'cadastro-turma',
        form: <>
                <div className="field-group">
                    <Field name="name" className="field" placeholder="Nome"/>
                </div>
        </>,
        actions: [
            {
                path: 'cadastro-turma',
                icon: <FaIcons.FaSearch />,
                color: 'green'
            },
            {
                path: 'cadastro-matricula',
                icon: <BiIcons.BiGroup />,
                color: 'orange'
            },
            {
                path: 'cadastro-turma-ocorrencia',
                icon: <FaIcons.FaListAlt />,
                color: 'white'
            }
        ]
    }

    return <DataTable configurations={ configuraciones}/>
}

export default ListaTurma