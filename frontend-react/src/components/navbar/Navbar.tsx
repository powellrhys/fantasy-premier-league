import { Link } from "react-router-dom"
import './Navbar.css'

export default function Navbar() {
    return (
        <nav className="nav">
            <Link to="/" className="home-title">FPL Dashboard</Link>
            <ul>
                <li><Link to="/player-analysis">Player Analysis</Link></li>
                <li><Link to="/goal-keeper-analysis">GK Analysis</Link></li>
                <li><Link to="/chip-analysis">Chip Analysis</Link></li>
            </ul>
        </nav>
    )
}
