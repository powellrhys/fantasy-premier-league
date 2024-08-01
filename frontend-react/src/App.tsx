import './App.css'
import Navbar from './components/navbar/Navbar'
import Home from "./pages/Home"
import GoalKeeperAnalysis from './pages/GoalKeeperAnalysis'
import { Route, Routes } from "react-router-dom"
import PlayerValue from './pages/PlayerValue'
import ChipAnalysis from './pages/ChipAnalysis'

function App() {

  return (
    <>
      <Navbar />
      <div className="container">
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/player-analysis" element={<PlayerValue />} />
          <Route path="/goal-keeper-analysis" element={<GoalKeeperAnalysis />} />
          <Route path="/chip-analysis" element={<ChipAnalysis />} />
        </Routes>
      </div>
    </>
  )
}

export default App