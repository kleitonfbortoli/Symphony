import React from 'react'
import ReactDOM from 'react-dom'

import App from './containers/App'

import 'normalize.css'
import './styles/scss/index/index.scss'

ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  document.getElementById('root')
)