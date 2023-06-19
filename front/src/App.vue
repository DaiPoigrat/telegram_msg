<template>
  <el-form
    label-position="top"
    label-width="100px"
    :model="formData"
    style="width: 1000px;"
  >
    <el-row :gutter="20">
      <el-col :span="10">
        <el-form-item label="Bot Token">
          <el-input v-model="formData.token" placeholder="TELEGRAM_BOT_TOKEN"/>
        </el-form-item>
      </el-col>
      <el-col :span="10">
        <el-form-item label="Chat ID">
          <el-input v-model="formData.chat_id" placeholder="Telegram chat id"/>
        </el-form-item>
      </el-col>
    </el-row>
    <el-row>
      <el-col :span="24">
        <el-form-item>
            <el-button 
            plain 
            @click="onSubmit"
            bg
            color="#409eff"
            dark
          >
            Save
          </el-button>
        </el-form-item>
      </el-col>
    </el-row>
  </el-form>
</template>

<script lang="ts" setup>
import { reactive } from 'vue';
import axios from 'axios';

const formData = reactive({
  token: '',
  chat_id: ''
})

axios.get('http://127.0.0.1:8000/send')
.then(function (response) {
  formData.token = response.data.saved_params.bot_token;
  formData.chat_id = response.data.saved_params.chat_id;
})

const onSubmit = () => {
  axios({
    method: 'post',
    url: 'http://127.0.0.1:8000/send',
    data: {
      token: formData.token,
      chat_id: formData.chat_id
    }
  })
  .then(function (response) {
    console.log(response);
  })
  .catch(function (error) {
    console.log(error);
  });
}


</script>

<style>
body {
  background-color: #18222c;
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  margin: 0;
}

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  display: flex;
  align-items: center;
}

.el-form-item__label {
  color: #fff;
  font-size: 15px;
}

.el-input__wrapper {
  background-color: #18222c;
  border-radius: 15px;
  height: 40px;
}

/* .el-button {
  background-color: #202020;
}
.el-button:hover {
  background-color: #202020;
} */
</style>
