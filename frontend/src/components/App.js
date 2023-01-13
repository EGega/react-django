import React from 'react'
import Headers from './layout/Headers.jsx'
import Dashboard from './leads/Dashboard.jsx'

const App = () => {
  return (
    <div>
      <Headers />
      <div className="container">
        <Dashboard />
      </div>
   
    </div>
  )
}

export default App