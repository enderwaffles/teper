import { createRouter, createWebHistory } from "vue-router"

import Home from "@/pages/Home.vue"
import About from "@/pages/About.vue"
import Login from "@/pages/auth/Login.vue"
import Signup from "@/pages/auth/Signup.vue"
import Posts from "@/pages/posts/Posts.vue"
import Post from "@/pages/posts/Post.vue"
import Create_post from "@/pages/posts/Create_post.vue"

const routes = [
    { path: '/', component: Home },
    { path: '/about', component: About },
    { path: '/login', component: Login },
    { path: '/signup', component: Signup },
    { path: '/posts', component: Posts },
    { path: '/posts/:id', component: Post },
    { path: '/create_post', component: Create_post },


    
]


const router = createRouter(
    {
        history: createWebHistory(),
        routes,
    }
)

export default router;