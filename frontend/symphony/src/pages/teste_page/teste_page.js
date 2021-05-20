import React from 'react'
import DataTable from '../../components/datatable/datatable'
import { POST_LIST_PESSOA } from '../../system/constants'
import {Field} from 'formik'
import * as AiIcons from 'react-icons/ai'

const teste_page = () => {
    let configuraciones = {
        page_size: 3,
        url: POST_LIST_PESSOA,
        form:
            <>
                <div className="field-group">
                    <Field name="nome" className="field" placeholder="Nome"/>
                </div>
                <div className="field-group">
                    <Field name="email" className="field" placeholder="E-mail"/>
                </div>
            </>,
        actions: [
            {
                path: 'cadastro-pessoa',
                icon: <AiIcons.AiFillHome />,
                // title: 'action teste',
                // parameters: '&teste=a'

            }
        ]
        
        
    }

    return <DataTable configurations={ configuraciones}/>
}

export default teste_page