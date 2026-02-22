import { createRouter, createWebHistory } from "vue-router"
import { useAuthStore } from "@/stores/auth";

import Home from "@/pages/Home.vue"
import About from "@/pages/About.vue"
import Login from "@/pages/auth/Login.vue"
import Signup from "@/pages/auth/Signup.vue"
import Posts from "@/pages/posts/Posts.vue"
import Post from "@/pages/posts/Post.vue"
import Create_post from "@/pages/posts/Create_post.vue"
import MyProfile from "@/pages/auth/MyProfile.vue";
import Update_post from "@/pages/posts/Update_post.vue";
import Verify from "@/pages/auth/Verify.vue";
import Forgot1 from "@/pages/auth/Forgot1.vue";
import Forgot2 from "@/pages/auth/Forgot2.vue";

const routes = [
    { path: '/', component: Home },
    { path: '/about', component: About },

    { path: '/login', component: Login },
    { path: '/signup', component: Signup },
    { path: '/verify', component: Verify },
    { path: '/forgot1', component: Forgot1 },
    { path: '/forgot2', component: Forgot2 },
    { path: '/myprofile', component: MyProfile, meta: { requiresAuth: true } },

    { path: '/posts', component: Posts },
    { path: '/posts/:id', component: Post },
    { path: '/create_post', component: Create_post, meta: { requiresAuth: true } },
    { path: '/update_post/:id', component: Update_post, meta: { requiresAuth: true } },


    
]


const router = createRouter(
    {
        history: createWebHistory(),
        routes,
    }
)

router.beforeEach((to, from, next) => {
  const auth = useAuthStore();

  if (to.meta.requiresAuth && !auth.session) {
    next("/login");
  } else {
    next();
  }
});


export default router;