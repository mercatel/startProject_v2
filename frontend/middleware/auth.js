import {useAuthStore} from "../stores/auth";

export default defineNuxtRouteMiddleware(async (to) => {
    const authStore = useAuthStore()
    if (process.client) {
        // Инициализируем аутентификацию при первом посещении
        if (!authStore.user) {
            await authStore.initStore()
        }

        // Если пользователь аутентифицирован и пытается попасть на страницу входа
        if (authStore.user && to.path === '/login') {
            return navigateTo('/')
        }

        // Если маршрут требует аутентификации и пользователь не аутентифицирован
        if (to.meta.requiresAuth && !authStore.user) {

            return navigateTo('/login')
        }
    }
})