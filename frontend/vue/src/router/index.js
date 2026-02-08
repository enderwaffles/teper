import { createRouter, createWebHistory } from "vue-router";

import Home from "../views/main/Home.vue";
import About from "../views/main/About.vue";
import Empty from "../views/main/Empty.vue";
import Posts from "../views/posts/Posts.vue";
import Post from "../views/posts/Post.vue";

export default createRouter({
  history: createWebHistory(),
  routes: [
    { path: "/", component: Home },
    { path: "/about", component: About },
    { path: "/posts", component: Posts },
    { path: "/posts/:id", component: Post },

    { path: "/empty", component: Empty, meta: { main: false } },
  ],
});
