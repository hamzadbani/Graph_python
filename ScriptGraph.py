#coding:utf-8 
#HAMZA DBANI MASTER SIM
import networkx as nx 
import matplotlib.pyplot as plt
class graph():
    #Le constructeur
    def __init__(self):
        print('------------------------Bienvenu dans le monde des graphes--------------------------')
        self.G=nx.Graph()
        self.G1=nx.DiGraph()
        self.liste= []
    #méthode pour choisir le type de graph (orienté/non orienté)
    def choixDegraph(self):
        print('''
           pour créer un graphe non orienté Tapez :1
           pour créer un graphe orienté Tapez :2
        ''')
        choix=int(input("Tapez votre choix : "))
        print("------------------------------------------------------")
        return choix
    #méthode pour créer Trois listes une pour les somments la deuxieme pour les somments qui seront liés avec la premiere liste et la derniere pour les couts
    #les trois listes seront zipé dans une seul liste qui sera notre graphe
    def createListe(self):
        listA = []
        listB = []
        listC = []
        n = int(input("Entrer le nombre des sommets dans le graph : "))
        for i in range(0, n):
            print("Entrer le sommet No-{}: ".format(i+1))
            var1="R"+str(input())
            listA.append(var1)
            print("Entrer le sommet a lié avec se sommet No-{}: ".format(i+1))
            var2="R"+str(input())
            listB.append(var2)
            print("Entrer le cout entre les deux sommet ")
            elm3 = int(input())
            listC.append(elm3)     
        self.liste =list(zip(listA,listB,listC))
    #méthode pour créer et afficher le graphe entrer par l'utilisateur
    def creategraph(self,choix):
        if choix==1:
            self.G.add_weighted_edges_from(self.liste)
            pos=nx.spring_layout(self.G)
            nx.draw(self.G,pos,with_labels=True,node_size=1500,node_color='yellow')
            nx.draw_networkx_edge_labels(self.G,pos,font_size=10,edge_labels=nx.get_edge_attributes(self.G,'weight'))
            plt.show()
        elif choix==2:
            self.G1.add_weighted_edges_from(self.liste)
            pos=nx.spring_layout(self.G1)
            nx.draw(self.G1,pos,with_labels=True,node_size=1500,node_color='yellow')
            nx.draw_networkx_edge_labels(self.G1,pos,font_size=10,edge_labels=nx.get_edge_attributes(self.G1,'weight'))
            plt.show()
    #méthode responsable d'afficher les caracteristique d'un graph (la taille,l'ordre,la densité,diametre,la matrice d'adjacence)        
    def caracteristique(self,choix):
        if choix==1:
            taille = len(self.liste);
            ordre = len(self.liste);
            print("• La Taille du graphe : {}".format(taille));
            print("• L'ordre'du graphe : {}".format(ordre));
            print("• La densité du graphe est : {}".format(2*abs(taille)/(abs(ordre)*(abs(ordre)-1))));
            print("• Les degrées des noeuds du graphe : ")
            print(self.liste)
            print("• Le diamètre est : {} ".format(nx.diameter(self.G)));
            print("Matrice d'adjacence")
            A=nx.adjacency_matrix(self.G)
            print(A.todense())
        if choix==2:
            taille = len(self.liste);
            ordre = len(self.liste);
            print("• La Taille du graphe : {}".format(taille))
            print("• L'ordre'du graphe : {}".format(ordre))
            print("• La densité du graphe est : {}".format(2*abs(taille)/(abs(ordre)*(abs(ordre)-1))));
            print("• Les degrées des noeuds du graphe : ")
            print(self.liste)
            #print("• Le diamètre est : {} ".format(nx.diameter(self.G1)))
            #print("• Le diamètre est : {} ".format(nx.diameter(net.to_undirected(self.G1))))
            print("Matrice d'adjacence")
            A=nx.adjacency_matrix(self.G1)
            print(A.todense())
    #Algorithme de  DFS:parcours en profondeur
    def AlgoDFS(self,choix):
        if choix==1:
            self.G.add_weighted_edges_from(self.liste)
            pos=nx.spring_layout(self.G)
            DFS=nx.depth_first_search.dfs_tree(self.G)
            plt.figure()
            plt.subplot(121)
            nx.draw(DFS,with_labels=True,node_size=600,node_color='yellow')
            plt.subplot(122)
            nx.draw(self.G,with_labels=True,node_size=600,node_color='yellow')
            plt.show()
        elif choix==2:
            self.G1.add_weighted_edges_from(self.liste)
            pos=nx.spring_layout(self.G1)
            DFS=nx.depth_first_search.dfs_tree(self.G1)
            plt.figure()
            plt.subplot(121)
            nx.draw(DFS,with_labels=True,node_size=600,node_color='yellow')
            plt.subplot(122)
            nx.draw(self.G1,with_labels=True,node_size=600,node_color='yellow')
            plt.show()
    #Algorithme de  BFS:parcours en largeur
    def AlgoBFS(self,choix):
        if choix==1:
            self.G.add_weighted_edges_from(self.liste)
            pos=nx.spring_layout(self.G)
            BFS=nx.breadth_first_search.bfs_tree(self.G,'R1')
            plt.figure()
            plt.subplot(121)
            nx.draw(BFS,with_labels=True,node_size=600,node_color='yellow')
            plt.subplot(122)
            nx.draw(self.G,with_labels=True,node_size=600,node_color='yellow')
            plt.show()
        elif choix==2:
            self.G1.add_weighted_edges_from(self.liste)
            pos=nx.spring_layout(self.G1)
            BFS=nx.breadth_first_search.bfs_tree(self.G1,'R1')
            plt.figure()
            plt.subplot(121)
            nx.draw(BFS,with_labels=True,node_size=600,node_color='yellow')
            plt.subplot(122)
            nx.draw(self.G1,with_labels=True,node_size=600,node_color='yellow')
            plt.show()
    #Algorithme de  Dijikstra:la recherche de plus court chemin
    def Dijikstra(self,choix):
        if choix==1:
            self.G.add_weighted_edges_from(self.liste)
            pos=nx.spring_layout(self.G)
            print("Entrer la source  : ")
            var1="R"+str(input())
            print("Entrer la destination  : ")
            var2="R"+str(input())
            if var1 not in self.G or var2 not in self.G:
                print("la source ou la destination spécifier n'existe pas")
            elif  nx.has_path(self.G,source=var1,target=var2)==True:
                print("le chemin le plus court est " ,nx.shortest_path(self.G,source=var1,target=var2))
                nx.draw(self.G,pos,with_labels=True,node_size=1500,node_color='yellow')
                nx.draw_networkx_edge_labels(self.G,pos,font_size=10,edge_labels=nx.get_edge_attributes(self.G,'weight'))
                plt.show()
            elif nx.has_path(self.G,source=var1,target=var2)==False:
                print('pas de chemin entre la source et la destination')
        if choix==2:
            self.G1.add_weighted_edges_from(self.liste)
            pos=nx.spring_layout(self.G1)
            print("Entrer la source  : ")
            var1="R"+str(input())
            print("Entrer la destination  : ")
            var2="R"+str(input())
            if var1 not in self.G1 or var2 not in self.G1:
                print("la source ou la destination spécifier n'existe pas")
            elif  nx.has_path(self.G1,source=var1,target=var2)==True:
                print("le chemin le plus court est ",nx.shortest_path(self.G1,source=var1,target=var2))
                nx.draw(self.G1,pos,with_labels=True,node_size=1500,node_color='yellow')
                nx.draw_networkx_edge_labels(self.G1,pos,font_size=10,edge_labels=nx.get_edge_attributes(self.G1,'weight'))
                plt.show()
            elif nx.has_path(self.G1,source=var1,target=var2)==False:
                print('pas de chemin entre la source et la destination')
    #Algorithme de  Bellman Ford:la recherche de plus court chemin           
    def BellmanFord(self,choix):
        if choix==1:
            self.G.add_weighted_edges_from(self.liste)
            pos=nx.spring_layout(self.G)
            print("Entrer la source  : ")
            var1="R"+str(input())
            print("Entrer la destination  : ")
            var2="R"+str(input())
            if var1 not in self.G or var2 not in self.G:
                print("la source ou la destination spécifier n'existe pas")
            elif  nx.has_path(self.G,source=var1,target=var2)==True:
                print("le chemin le plus court est " ,nx.bellman_ford_path(self.G,source=var1,target=var2))
                nx.draw(self.G,pos,with_labels=True,node_size=1500,node_color='yellow')
                nx.draw_networkx_edge_labels(self.G,pos,font_size=10,edge_labels=nx.get_edge_attributes(self.G,'weight'))
                plt.show()
            elif nx.has_path(self.G,source=var1,target=var2)==False:
                print('pas de chemin entre la source et la destination')

        if choix==2:
            self.G1.add_weighted_edges_from(self.liste)
            pos=nx.spring_layout(self.G1)
            print("Entrer la source  : ")
            var1="R"+str(input())
            print("Entrer la destination  : ")
            var2="R"+str(input())
            if var1 not in self.G1 or var2 not in self.G1:
                print("la source ou la destination spécifier n'existe pas")
            elif  nx.has_path(self.G1,source=var1,target=var2)==True:
                print("le chemin le plus court est ",nx.bellman_ford_path(self.G1,source=var1,target=var2))
                nx.draw(self.G1,pos,with_labels=True,node_size=1500,node_color='yellow')
                nx.draw_networkx_edge_labels(self.G1,pos,font_size=10,edge_labels=nx.get_edge_attributes(self.G1,'weight'))
                plt.show()
            elif nx.has_path(self.G1,source=var1,target=var2)==False:
                print('pas de chemin entre la source et la destination')
    #algorithme de Kruskal pour construire l'arbre minimal à partir du plus petit cout
    def Kruskal(self,choix):
        if choix==1:
            self.G.add_weighted_edges_from(self.liste)
            pos=nx.spring_layout(self.G)
            GKruskal=nx.minimum_spanning_tree(self.G)
            plt.figure()
            plt.subplot(121)
            nx.draw(GKruskal,pos,with_labels=True,node_size=600,node_color='yellow')
            nx.draw_networkx_edge_labels(GKruskal,pos,font_size=10,edge_labels=nx.get_edge_attributes(self.G,'weight'))
            plt.subplot(122)
            nx.draw(self.G,pos,with_labels=True,node_size=600,node_color='yellow')
            nx.draw_networkx_edge_labels(self.G,pos,font_size=10,edge_labels=nx.get_edge_attributes(self.G,'weight'))
            plt.show()
    #méthode pour calculer le graph transitif a partir d'un graph orienté
    def transitive(self,choix):
        if choix==2:
            self.G1.add_weighted_edges_from(self.liste)
            pos=nx.spring_layout(self.G1)
            Gtransitive=nx.transitive_closure(self.G1)
            plt.figure()
            plt.subplot(121)
            nx.draw(Gtransitive,pos,with_labels=True,node_size=600,node_color='yellow')
            nx.draw_networkx_edge_labels(Gtransitive,pos,font_size=10,edge_labels=nx.get_edge_attributes(self.G1,'weight'))
            plt.subplot(122)
            nx.draw(self.G1,pos,with_labels=True,node_size=600,node_color='yellow')
            nx.draw_networkx_edge_labels(self.G1,pos,font_size=10,edge_labels=nx.get_edge_attributes(self.G1,'weight'))
            plt.show()

G=graph()
n=-1
while n!=0:
    print('''
        pour créer et visualiser un graphe Tapez :1
        pour appliquer l'algorithme DFS sur un graphe Tapez :2
        pour appliquer l'algorithme BFS sur un graphe Tapez :3
        pour appliquer l'algorithme Dijikstra sur un graphe Tapez :4
        pour appliquer l'algorithme Bellman Ford sur un graphe Tapez :5
        pour appliquer l'algorithme Kruskal  sur un graphe Tapez :6
        caractéristique du graphe :7
        pour visualiser le graphe transitif Tapez:8
        pour quiter tapez :0
    ''')
    try :
        menu=int(input("Tapez votre choix : "))
        if menu==1:
            ch=G.choixDegraph()
            if ch==1 or ch==2:
                G.createListe()
                G.creategraph(ch)
            else:
                print("ce n'est pas le bon choix")      
        elif menu==2:
            try :
                G.AlgoDFS(ch)
            except Exception:
                print ("Il faut tout d'abord créer un graph  !")      
        elif menu==3:
            try :
                G.AlgoBFS(ch)
            except Exception:
                print ("Il faut tout d'abord créer un graph  !")
        elif menu==4:
            try :
                G.Dijikstra(ch)
            except Exception:
                print ("Il faut tout d'abord créer un graph  !")
        elif menu==5:
            try :
                G.BellmanFord(ch)
            except Exception:
                print ("Il faut tout d'abord créer un graph  !")
        elif menu==6:
            try :
                if ch==1:
                    G.Kruskal(ch)
                elif ch==2:
                    print("vous ne pouvez pas appliquer l'algorithme de Kruskal sur un graph orienté")
            except Exception:
                print ("Il faut tout d'abord créer un graph  !")
        elif menu==7:
            try :
                G.caracteristique(ch)
            except Exception:
                print ("Il faut tout d'abord créer un graph  !")
        elif menu==8:
            try :
                if ch==1:
                    print (" le graphe transitif non implémenté pour le type non orienté   !")
                if ch==2:
                    G.transitive(ch)
            except Exception:
                print ("Il faut tout d'abord créer un graph  !")
        elif menu==0:
            n=0
        else:
            print("ce n'est pas le bon choix")
    except ValueError:
        print ("entrer une valide valeur !")

