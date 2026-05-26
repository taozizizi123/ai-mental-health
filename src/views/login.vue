<template>
    <div class="container">
        <div class="title">
            <div class="back-home"  @click="goHome" style="cursor: pointer;">
                <el-icon><Back /></el-icon>
                <span>返回首页</span>
            </div>
            <div class="title-text">
                <h2>登录您的账户</h2>
                <p>请输入您的登录信息</p>
            </div>
        </div>
        <div class="form-container">
            <el-form
                ref="ruleFormRef"
                :model="formData"
                :rules="rules"
                label-position="top"
            >
                <el-form-item label="用户名或邮箱" prop="username">
                    <el-input v-model="formData.username" size="large" placeholder="请输入用户名" />
                </el-form-item>
                <el-form-item label="密码" prop="password">
                    <el-input v-model="formData.password" size="large" placeholder="请输入密码" type="password" show-password />
                </el-form-item>
                <el-button class="btn" size="large" type="primary" @click="submitForm(ruleFormRef)">登录账户</el-button>
            </el-form>
            <div class="footer">
                <p>还没有账号？<router-link to="/auth/register">去注册</router-link></p>
            </div>
        </div>
    </div>
</template>
<script setup>
import { ref, reactive } from 'vue'
import { ElMessage } from 'element-plus'
import { login } from '@/api/admin'
import { useRouter } from 'vue-router'
import { Back } from '@element-plus/icons-vue'

const ruleFormRef = ref()

const formData = reactive({
    username: '',
    password: ''
})
const rules = reactive({
    username: [
        { required: true, message: '请输入用户名', trigger: 'blur' }
    ],
    password: [
        { required: true, message: '请输入密码', trigger: 'blur' }
    ]
})

const router = useRouter()

//返回首页
const goHome = () => {
    router.push('/')
}



const submitForm = async (formEl) => {
    if (!formEl) return
    await formEl.validate((valid, fields) => {
        if (valid) {
            login(formData).then(data => {
                //判断token是否存在
                if (!data.token) {
                    return console.error('登录失败')
                }
                //登录成功，保存token用户信息
                localStorage.setItem('token', data.token)
                localStorage.setItem('userInfo', JSON.stringify(data.userInfo))
                //根据用户角色决定跳转的路径
                if (data.userInfo.userType === 2) {
                    router.push('/back/dashboard')
                } else {
                    router.push('/')
                }
            })
        }
    })
}
</script>
<style scoped lang="scss">
    .container {
        width: 384px;
        .title {
            .back-home {
                margin-bottom: 60px;
            }
            .title-text {
                text-align: center;
                h2 {
                    font-size: 42px;
                    font-weight: bold;
                    margin-bottom: 16px;
                }
                p {
                    font-size: 20px;
                    color: #6b7280;
                    margin-bottom: 24px;
                }
            }
        }
        .form-container {
            margin-top: 30px;
            :deep(.el-form-item__label) {
                font-size: 18px;
                font-weight: 300;
                color: #374151;
                margin-bottom: 12px;
            }
            
            :deep(.el-input__wrapper) {
                font-size: 15px;
                padding: 14px 16px;
            }
            
            :deep(.el-input__inner) {
                font-size: 15px;
                height: 20px;
                line-height: 20px;
            }
            
            :deep(.el-input::placeholder) {
                font-size: 15px;
                color: #9ca3af;
            }

            .btn{
                margin-top: 40px;
                width: 100%;
            }
            .footer {
                padding: 30px;
                text-align: center;
            }
        }
    }
</style>
