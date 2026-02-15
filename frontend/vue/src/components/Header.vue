<template>

<header class="header">

<div class="part">
    <h1>Forgeswords</h1>
</div>

<div class="part">
    <RouterLink class="nav-link" to="/">Home </RouterLink>
    <RouterLink class="nav-link" to="/about">About </RouterLink>
    <RouterLink class="nav-link" to="/posts">Posts </RouterLink>
    <RouterLink v-if="auth.session" to="/create_post">Create post </RouterLink>
</div>

<div class="part">
    <div v-if="!auth.session">
        <RouterLink class="auth-link signup-btn" to="/signup">Sign up </RouterLink>
        <RouterLink class="auth-link" to="/login">Login </RouterLink>
    </div>  

    <div v-else>
        <RouterLink class="auth-link" to="/profile">Profile</RouterLink>
    </div>
</div>


</header>

</template>

<script setup>
import Signup from '@/pages/auth/Signup.vue';
import { useAuthStore } from '@/stores/auth'
const auth = useAuthStore()
</script>

<style scoped>

h1 {
    color: coral;
}

.header {
    display: flex;
    align-items: center;
    padding: 15px 30px; 

    background: rgb(20, 20, 20);
    border-bottom: 1px solid rgb(30, 30, 30);
}

/* Лого */
.part:first-child h1 {
    font-size: 22px;
    margin: 0;
}

/* Центр (меню) */
.part:nth-child(2) {
    flex: 1;

    display: flex;
    justify-content: center;
    gap: 25px;
}

/* Право (логин / профиль) */
.part:last-child {
    display: flex;
    justify-content: flex-end;
}

/* Все ссылки */
.header a {
    text-decoration: none;
    color: rgb(200, 200, 200);

    padding: 6px 10px;
    border-radius: 10px;

    transition: 0.4s;
}

/* Наведение */
.header a:hover {
    background: rgb(50, 50, 50);
}

.router-link-exact-active {
  background: rgba(255, 127, 80, 0.25);
  color: white;
}


/* Мобильная версия */
@media (max-width: 768px) {

  .header {
    flex-direction: column;
    gap: 15px;
    padding: 15px;
  }

  /* Центрируем всё */
  .part {
    width: 100%;
    display: flex;
    justify-content: center;
  }

  /* Меню */
  .part:nth-child(2) {
    flex-wrap: wrap;
    gap: 15px;
  }

  /* Правый блок */
  .part:last-child {
    justify-content: center;
  }
}


</style>
