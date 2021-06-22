import React, { useEffect, useState } from 'react'

import DataTableBody from './datatablebody'
import DataTableHeader from './datatableheader'
import DataTableNavigation from './datatablenavigation'

import Select from 'react-select'
import * as FaIcons from 'react-icons/fa'

import { Formik, Form } from 'formik'
import { System } from '../../system/system'

import '../../styles/scss/custon-select/custon.scss'
import '../../styles/scss/pages/datatable/datatable.scss'

require("es6-promise").polyfill()

// usado para criar cadastros n para n
export default function GroupForm({ configurations }) {

    const [api_data, setApiData] = useState({
        header:[],
        body: [
            {
                data: [],
                key: 0
            }
        ],
        count_results : 0
    })

    const [page_number, setPageNumber] = useState(1)
    const [combo_itens, setComboItens] = useState([])
    
    function reloadDataGrid(page_number) {
        
        setPageNumber(page_number)
        
        let post_data = {
            page_number: page_number,
            page_size: configurations.page_size,
            key: configurations.key // chave do objeto
        };

        System.post(configurations.url_get_list, post_data, (data) => {
            setApiData(data)
        });
    }

    function reloadComboItens()
    {
        let parans = {
            key: configurations.key

        }
        System.post(configurations.url_get_combo_itens, parans, (data) => {
            setComboItens(data)
        });
    }

    function cadastrarDado(form_data)
    {
        
        form_data.preventDefault()
        form_data.stopPropagation();
        console.log(form_data.target)
        let parans = {
            key: configurations.key,
            relation:  form_data.target[1].value
        }

        if (typeof configurations.extra_fields !== 'undefined') {
            configurations.extra_fields.map((field_name) =>
            {
                parans[field_name] = form_data.target[field_name].value
            })
        }

        System.post(configurations.url_cadastro, parans, () => {
            reloadComboItens()
            reloadDataGrid(page_number)
        });
        }

    function DeletaDado(key)
    {
        let parans = {
            key: key
        }
        System.post(configurations.url_delete_cadastro, parans, () => {
            reloadComboItens()
            reloadDataGrid(page_number)
        });
    }
    
    useEffect(() => {
        reloadDataGrid(1)
        reloadComboItens()
    }, [])

    const change_function = (value) => {
        reloadDataGrid(value.target.value)
    }

    configurations.actions = [
        {
            click: DeletaDado,
            icon: <FaIcons.FaTrash />,
            color: 'red'
        }
    ];
    if (typeof configurations.extra_fields === 'undefined') {
        configurations.extra_fields = [];
    } 

    if (typeof configurations.extra_actions !== 'undefined')
    {
        configurations.actions = configurations.actions.concat(configurations.extra_actions)
    }
    
    const theme = (theme) => ({
      ...theme,
      borderRadius: 0,
      colors: {
        ...theme.colors,
        primary25: 'blue',
        primary: 'blue',
      },
    })
    

    return <>
        <div className="datatable">
            <div className="form">
                <h1 className="form-title">{configurations.title}</h1>
                <form className="form-body" onSubmit={cadastrarDado}>
                    <Select options={combo_itens} name="relation" placeholder="Selecionar" className="search-combo" theme={theme} />
                    {
                        configurations.extra_fields.map((field_name) => {
                            return <input name={ field_name}></input>
                        })
                    }
                    <button className="submit-button" type="submit">Cadastrar</button>
                </form>
            </div>
            <table className="datatable-table">
                <DataTableHeader data={api_data} configurations={configurations } />
                <DataTableBody data={api_data} configurations={configurations } />
                <DataTableNavigation data={api_data} configurations={configurations} page_number={page_number} change_function={change_function} />
            </table>
        </div>
    </>
}