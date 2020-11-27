import React from 'react'
import { faBars, faHome, faListAlt, faMoneyCheckAlt, faShoppingBasket, faTicketAlt, faTruckMoving, faUserCircle } from '@fortawesome/free-solid-svg-icons'


export const SidebarData =[
    {
        title:'Home',
        path:'/Dashboard',
        cName:'sidebar-item',
        icon: faHome

    },
    {
        title:'Booking',
        path:'/Dashboard/Booking',
        cName:'sidebar-item',
        icon: faTicketAlt

    },
    {
        title:'Account',
        path:'/Dashboard/Account',
        cName:'sidebar-item',
        icon: faUserCircle


    }


]