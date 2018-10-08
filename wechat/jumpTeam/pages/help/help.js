Page({

  /**
   * 页面的初始数据
   */
  data: {
    id:0,
    command:{
      start:'点击蓝色小方块定义矩阵，使用已经定义好的矩阵(如m1)在蓝色小方块下方写入计算表达式,最后点击计算结果，得到答案。',
      title0:'下面是功能使用介绍',
      mult:'1.矩阵的乘法 ',
      multsol:'m1*m2',
      T:'2.计算m1的转置',
      Tsol:'m1.T',
      H:'3.计算m1的共轭转置',
      Hsol:'m1.H',
      I:'4.计算m1的逆矩阵',
      Isol:'m1.I',
      title1:'使用Python的linalg库来解决更加复杂的问题,已做简化调用',
      tez:'5.计算矩阵m1的特征值',
      tezsol:'ng.eigvals(m1) ',
      tezx:'6.计算特征值和对应特征向量，第一个为特征值，第二个为特征向量',
      tezxsol:'ng.eig(m1) ',
      hls:'7.计算矩阵m1的行列式',
      hlsol:' ng.det(m1)',
      ni:'8.计算矩阵m1的逆矩阵',
      nisol:'ng.inv(m1)',
      zhi:'9.计算矩阵m1的秩',
      zhisol:'ng.matrix_rank(m1)',
      fczitle:'10.解方程组',
      fcz:'形如 m1x = m2 的线性方程组，其中 m1 为矩阵，m2 为一维或二维的数组，x 是未知变量',
      matrix0:'m1 = [[1,-2,1],',
      matrix1:'[0,2,-8],',
      matrix2:'[-4,5,9]]',
      matrix3:'m2 = [0,8,-9]',
      fczsol:'ng.solve(m1,m2.T)',
      SVD:'11.SVD是一种因子分解运算，将一个矩阵分解为3个矩阵的乘积,得到3个矩阵——U、Sigma和V，其中U和V是正交矩阵，Sigma包含输入矩阵的奇异值。',
      SVDsol:'ng.SVD(m1)',


    },
    matrix:{
      start:'矩阵的每一行使用"[ ]"包裹起来，数字之间使用","分隔开，如下是一个2X2的矩阵：',
      matrix0: '[[1,2],',
      matrix1: '[3,4]]',
      enter:'Enter键为换行键',
      end:'矩阵输入完成后，点击ok，完成对矩阵的定义'
    },
    
    
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    // id == 0 为numpy操作指南 
    if(options.id==1){
      this.setData({
        id : 1
      })
    }
    
  },

  /**
   * 生命周期函数--监听页面初次渲染完成
   */
  onReady: function () {
    
  },

  /**
   * 生命周期函数--监听页面显示
   */
  onShow: function () {
    
  },

  /**
   * 生命周期函数--监听页面隐藏
   */
  onHide: function () {
    
  },

  /**
   * 生命周期函数--监听页面卸载
   */
  onUnload: function () {
    
  },

  /**
   * 页面相关事件处理函数--监听用户下拉动作
   */
  onPullDownRefresh: function () {
    
  },

  /**
   * 页面上拉触底事件的处理函数
   */
  onReachBottom: function () {
    
  },

  /**
   * 用户点击右上角分享
   */
  onShareAppMessage: function () {
    
  }
})