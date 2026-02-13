<template>
    <header class="header">

        <!-- Лого -->
        <div class="logo">
            <h1>Forgeswords</h1>
        </div>

        <!-- Навигация -->
        <nav class="nav">
            <RouterLink class="nav-link" to="/">Home</RouterLink>
            <RouterLink class="nav-link" to="/about">About</RouterLink>
            <RouterLink class="nav-link" to="/posts">Posts</RouterLink>

            <RouterLink v-if="auth.session" class="nav-link" to="/create_post">
                Create post
            </RouterLink>
        </nav>

        <!-- Авторизация -->
        <div class="auth">
            <template v-if="!auth.session">
                <RouterLink class="auth-link signup-btn" to="/signup">
                    Sign up
                </RouterLink>
                <RouterLink class="auth-link" to="/login">Login</RouterLink>
            </template>

            <template v-else>
                <RouterLink class="auth-link" to="/profile">{{ auth.user.name }}</RouterLink>
            </template>
        </div>

    </header>
</template>

<script setup>
import { useAuthStore } from '@/stores/auth'

const auth = useAuthStore()
</script>

<style scoped>
/* ===== БАЗА ===== */

.header {
    display: flex;
    align-items: center;
    justify-content: space-between;

    padding: 15px 40px;
    background: #222;
    color: white;

    position: sticky;
    top: 0;
    z-index: 1000;
}

.logo h1 {
    margin: 0;
    font-size: 22px;
    color: coral;
}


/* ===== НАВИГАЦИЯ ===== */

.nav {
    display: flex;
    gap: 25px;
}

.auth {
    display: flex;
    gap: 15px;
    align-items: center;
}


/* ===== ССЫЛКИ ===== */

.nav-link,
.auth-link {
    display: inline-flex;
    align-items: center;
    justify-content: center;

    color: white;
    text-decoration: none;
    font-weight: 500;

    padding: 6px 12px;
    border-radius: 6px;

    transition: all 0.2s ease;
}


/* Наведение */
.nav-link:hover,
.auth-link:hover {
    transform: scale(1.08);
    /* color: #38bdf8; */
    /* background: rgba(56, 189, 248, 0.15); */
}


/* Нажатие */
/* .nav-link:active,
.auth-link:active {
  color: #0ea5e9;
  background: rgba(14, 165, 233, 0.2);
} */


/* Активная страница */
.nav-link.router-link-active,
.auth-link.router-link-active {
    color: coral;
    background: rgba(255, 127, 80, 0.200);
}

/* Фиолетовая кнопка Sign up */
.signup-btn {
    background: linear-gradient(135deg, coral, purple);
    color: white;

    padding: 7px 16px;
    border-radius: 0px;

    font-weight: 600;
}

/* Hover */
.signup-btn:hover {
    background: linear-gradient(135deg, coral, purple);
    transform: scale(1.1);
    color: white;
}

/* Нажатие */
.signup-btn:active {
    background: linear-gradient(135deg, #7c3aed, #5b21b6);
    transform: scale(1.05);
}

</style>
