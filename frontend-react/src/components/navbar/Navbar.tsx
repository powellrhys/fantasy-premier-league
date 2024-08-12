import { NavLink } from "react-router-dom"
import './Navbar.css'

export default function Navbar() {

    const CustomNavLink = (
        {route, nav_text} :
        {route: string, nav_text: string}
    ) => {
        return (
            <li>
                <NavLink 
                    className={({ isActive }) =>
                        isActive ? "active-link" : "inactive-link"}
                    to={route}>
                        {nav_text}   
                </NavLink>
            </li>
        )
    }

    return (
        <nav className="nav">
            <NavLink to="/" className="home-title">FPL Dashboard</NavLink>
            <ul>
                <CustomNavLink 
                    route={'/player-analysis'} 
                    nav_text={'Player Analysis'}
                />
                <CustomNavLink 
                    route={'/goal-keeper-analysis'} 
                    nav_text={'GK Analysis'}
                />
                <CustomNavLink 
                    route={'/chip-analysis'} 
                    nav_text={'Chip Analysis'}
                />
            </ul>
        </nav>
    )
}
