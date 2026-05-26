<template>
  <div class="page-head">
    <p class="page-title">{{ props.title }}</p>
    <div class="action-btn">
        <slot name="action-btn"></slot>
    </div>
  </div>
</template>
<script setup>
const props = defineProps({
    title: {
        type: String,
        default: '页面标题'
    }
})
</script>
<style lang="scss" scoped>
.page-head {
    margin-bottom: 20px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    .page-title {
        font-size: 24px;
        font-weight: bold;
        color: #303133;
    }
    height: 60px;
    line-height: 60px;
    padding-left: 20px;
}
</style>