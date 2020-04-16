import Mock from 'mockjs'

Mock.mock(/getNewsList/,{
    'list|5':[
        {
        url:'@url',     // 加 @  自动生成链接
        title:'@ctitle(5,20)'    // 加@c  制动生成  5-20  的 标题
        }
    ]
})

Mock.mock(/getProductList/,{
    pc: {
        title: "@ctitle(4)",
        list: [
          {
            title: "@ctitle(4)",
            url: "@url"
          },
          {
            title: "@ctitle(4)",
            url: "@url"
          },
          {
            title: "@ctitle(4)",
            url: "@url",
            hot: '@boolean'
          },
          {
            title: "@ctitle(4)",
            url: "@url"
          }
        ]
    },
    app: {
        title: "@ctitle(4)",
        last:'@boolean',
        list: [
          {
            title: "@ctitle(4)",
            url: "@url",
          },
          {
            title: "@ctitle(4)",
            url: "@url",
            hot: '@boolean'
          },
          {
            title: "@ctitle(4)",
            url: "@url",
          },
          {
            title: "@ctitle(4)",
            url: "@url",
            hot: '@boolean'
          }
        ]
    }
})

Mock.mock(/getBoardList/,[
    {
        title:'@ctitle(4)',
        description:'@ctitle(8,12)',
        saleout:'@boolean',
    },
    {
        title:'@ctitle(4)',
        description:'@ctitle(8,12)',
        saleout:'@boolean',
    },
    {
        title:'@ctitle(4)',
        description:'@ctitle(8,12)',
        saleout:'@boolean',
    },
    {
        title:'@ctitle(4)',
        description:'@ctitle(8,12)',
        saleout:'@boolean',
    },
])
export default Mock     // 把Mock 对象 传递出去