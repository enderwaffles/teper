
import { defineStore } from "pinia";
import { ref } from "vue";
import { useRouter } from "vue-router";

const router = useRouter();

export const useAuthStore = defineStore("auth", () => {
    const session = ref(false);
    const user = ref(null);

    function login({ id, name}) {
        user.value = {id, name};
        session.value = true;
    }
    function logout() {
        user.value = null;
        session.value = false;
        router.push("/")
    }
    return {
        session, user, login, logout
    }

})

