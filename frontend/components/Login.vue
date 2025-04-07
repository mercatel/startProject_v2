<template>
  <div class="login">
    <form class="border" @submit.prevent="logIn">
      <div class="login__username">
        <v-text-field v-model="username" type='text' label="Логин" density="compact" variant="outlined" required/>
      </div>
      <div class="login__password">
        <v-text-field v-model="password" :type="typePassword" autocomplete="on" label="Пароль" density="compact"
                      variant="outlined"
                      required>
          <template v-slot:append-inner>
            <v-icon v-if="typePassword==='password'" icon="mdi-eye-off" @click.passive="typePassword='text'"></v-icon>
            <v-icon v-else icon="mdi-eye" @click.passive="typePassword='password'"></v-icon>
          </template>
        </v-text-field>
      </div>
      <div class="login__errors">
        <div v-for="item in errors">{{ item }}</div>
      </div>
      <div class="login__actions">
        <v-btn type="submit" variant="tonal" block size="40">Войти</v-btn>
      </div>
    </form>
  </div>
</template>

<script setup>
const auth = useAuthStore()
const router = useRouter()
const route = useRoute()

const username = ref("")
const password = ref("")
const typePassword = ref("password")
const errors = ref([])
const snackbar = ref({
  show: false,
  text: ''
})

async function logIn() {
  errors.value = []
  const response = await auth.logIn(route?.query?.path, {username: username.value, password: password.value})
  if (response === 401) {
    errors.value.push(`Не найдена активная учетная запись с указанными учетными данными`)
  }
}
</script>

<style scoped lang="scss">
.login {
  margin: auto;
  padding: 1%;
}

form {
  padding: 1%;
  margin: auto;
  width: 350px;

  .login__errors {
    min-height: 50px;
  }
}
</style>