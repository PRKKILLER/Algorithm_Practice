//
// Created by 薛智钧 on 2020/3/26.
//

#ifndef DATASTRUCTURE_BINNODE_MACRO_H
#define DATASTRUCTURE_BINNODE_MACRO_H
/*****************************************
 * BinNode状态与性质的判断
 *****************************************/
#define IsRoot(x) (!((x).parent)) // 不存在父节点
#define IsLChild(x) (! IsRoot(x) && (&(x) == (x).parent->lc))
#define IsRChild(x) (! IsRoot(x) && (&(x) == (x).parent->rc))
#define HasParent(x) (! IsRoot(x))
#define HasLChild(x) ((x).lc)
#define HasRChild(x) ((x).rc)
#define HasChild(x) (HasLChild || HasRChild(x))
#define IsLeaf(x) (! HasChild(x))

#define sibling(p) /*兄弟节点*/ \
   (IsLChild(*(p)) ? (p)->parent->rc : (p)->parent->lc)

#define uncle(x) /*叔叔*/ \
   ( IsLChild( * ( (x)->parent ) ) ? (x)->parent->parent->rc : (x)->parent->parent->lc )

#define FromParentTo(x) /*来自父亲的引用*/ \
   ( IsRoot(x) ? _root : ( IsLChild(x) ? (x).parent->lc : (x).parent->rc ) )


#endif //DATASTRUCTURE_BINNODE_MACRO_H
