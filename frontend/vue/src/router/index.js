import { createRouter, createWebHistory } from "vue-router"

import Home from "@/pages/Home.vue"
import About from "@/pages/About.vue"
import Login from "@/pages/auth/Login.vue"
import Signup from "@/pages/auth/Signup.vue"

const routes = [
    { path: '/', component: Home },
    { path: '/about', component: About },
    { path: '/login', component: Login },
    { path: '/signup', component: Signup },
    
]


const router = createRouter(
    {
        history: createWebHistory(),
        routes,
    }
)

export default router;