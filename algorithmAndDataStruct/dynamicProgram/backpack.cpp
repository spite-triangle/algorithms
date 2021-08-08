#include <iostream>
#include <string>
#include <vector>
#include <math.h>
using namespace std;

struct Goods{
    int v;
    int p;
    
    Goods(){
        this->v = 0;
        this->p = 0;
    }
    
    Goods(int v,int p){
        this->v = v/10;
        this->p = p * v / 10;
    }
};

struct Commodity{
    Goods m;
    Goods v1;
    Goods v2;
};


int main(){
    
    int total;
    int n;
    int count = 0;
    
    // 总价与商品数
    cin >> total >> n;
    total /= 10;
    
    vector<Commodity> com(n+1);
    //com.push_back(Commodity());
    
    // 添加货物
    for(int i = 1; i <= n; i++){
        int v,p,q;
        cin >> v >> p >> q;
        
        // 添加主件
        if(q == 0){
            //com.push_back(Commodity(Goods(v,p)));
            count ++;
            // i 不是主商品，count才是
            com[count].m = Goods(v,p);
            
        }else if(com[q].v1.p == 0){
            com[q].v1 = Goods(v,p);
        }else{
            com[q].v2 = Goods(v,p);
        }
    }
    
    vector< vector<int> > grid(count + 1,vector<int>(total+1,0));
    
    // 遍历主物品
    for(int i = 1; i <= count; i++ ){
        // 价格
        for(int r = 0;r <= total; r++){
            // 能放下
           if(com[i].m.v <= r){
               grid[i][r] = max(grid[i-1][r] , grid[i-1][r - com[i].m.v] + com[i].m.p);

               // 附属的情况
               if( com[i].v1.p != 0 && (com[i].v1.v + com[i].m.v <= r)){
                   grid[i][r] = max(grid[i][r] , grid[i-1][r - com[i].v1.v - com[i].m.v] + com[i].m.p + com[i].v1.p);
               }
               if(com[i].v2.p != 0 && (com[i].v2.v + com[i].m.v <= r)){
                   grid[i][r] = max(grid[i][r],grid[i-1][r - com[i].v2.v - com[i].m.v] + com[i].m.p + com[i].v2.p);
               }
               if(com[i].v1.p != 0 && com[i].v2.p != 0 && (com[i].v1.v + com[i].v2.v + com[i].m.v <= r)){
                   grid[i][r] = max(grid[i][r],grid[i-1][r - com[i].v1.v - com[i].v2.v - com[i].m.v] + com[i].m.p + com[i].v1.p + com[i].v2.p);
               }

           }else{
               grid[i][r] = grid[i-1][r];
           }
        }
        
    }
    
    cout << grid[count][total] * 10 << endl;
    
    
    return 0;
}