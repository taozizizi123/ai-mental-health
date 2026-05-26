<template>
  <div class="frontend-layout">
    <!-- 顶部导航 -->
    <div class="navbar-container">
      <div class="brand-section">
        <el-image 
          style="height: 50px; width: 50px" 
          :src="iconUrl" 
          alt="品牌logo" 
          class="brand-logo" 
        />
        <h1 class="brand-name">心理健康AI助手</h1>
      </div>
      
      <div class="nav-section">
        <router-link to="/" class="nav-link">首页</router-link>
        <router-link to="/consultation" class="nav-link" v-if="isLoggedIn">AI咨询</router-link>
        <router-link to="/emotion-diary" class="nav-link" v-if="isLoggedIn">情绪日记</router-link>
        <router-link to="/knowledge" class="nav-link">知识库</router-link>
        
        <el-button v-if="isLoggedIn" class="logout-btn" @click="handleLogout">退出登录</el-button>
        <template v-else>
          <router-link to="/auth/login" class="nav-link">登录</router-link>
          <router-link to="/auth/register" class="nav-link">
            <el-button type="primary">注册</el-button>
          </router-link>
        </template>
      </div>
    </div>
    
    <!-- 主内容区 -->
    <div class="main-content">
      <router-view></router-view>
    </div>
    
    <!-- 底部：只在首页显示 -->
    <div class="footer-container" v-if="$route.path === '/'">
      <div class="footer-bottom">
        <p>&copy; 2026 心理健康AI助手. All rights reserved</p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { logout } from '@/api/admin'

const router = useRouter()
const route = useRoute()

// 图标路径
const iconUrl = new URL('@/assets/images/机器人.png', import.meta.url).href

// 登录状态
const isLoggedIn = ref(false)

// 退出登录
const handleLogout = () => {
  logout().then(() => {
    // 清除缓存
    localStorage.removeItem('token')
    localStorage.removeItem('userInfo')
    // 跳转到登录页
    router.push('/auth/login')
  })
}

// 初始化
onMounted(() => {
  isLoggedIn.value = localStorage.getItem('token') !== null
})
</script>

<style lang="scss" scoped>
.frontend-layout {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  background-color: #fff;

  .navbar-container {
    max-width: 1400px;
    margin: 0 auto;
    padding: 10px 40px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    width: 100%;
    box-sizing: border-box;

    .brand-section {
      display: flex;
      align-items: center;
      margin-right: auto;

      .brand-logo {
        border-radius: 50%;
        background: rgba(74, 144, 226, 0.1);
        padding: 5px;
      }

      .brand-name {
        margin-left: 10px;
        font-size: 24px;
        font-weight: 600;
        color: #333;
      }
    }

    .nav-section {
      display: flex;
      align-items: center;
      gap: 40px;
      margin-left: auto;

      .nav-link {
        color: #4b5563;
        font-size: 20px;
        font-weight: 500;
        text-decoration: none;
        cursor: pointer;

        &:hover {
          color: #4A90E2;
        }
      }
    }
  }

  .main-content {
    flex: 1;
    width: 100%;
  }

  .footer-container {
    background: #1f2937;
    color: white;
    padding: 15px 0;
    margin-top: auto;
    flex-shrink: 0;

    .footer-bottom {
      max-width: 1200px;
      margin: 0 auto;
      padding: 0 20px;
      text-align: center;

      p {
        margin: 0;
        font-size: 14px;
        color: rgba(255, 255, 255, 0.8);
      }
    }
  }
}
</style>