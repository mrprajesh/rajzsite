Title: Research
Date: 20.12.2017 15:15:38
page-order: 3

I get excited about every aspect of Parallelization of Graph Algorithms on GPUs.
My **research area** includes 

- GPU Computing
- Graph Analytics
- Parallel and High-Performance Computing (HPC) 


<!--- I am really fortunate to have my Ph.D. advisors as [N.S. Narayanaswamy][1] (also my M.Tech. project's advisor) and [Rupesh Nasre][3].

Both of them are wonderful professors/researchers I have ever met. From them, I have not just learnt doing research but also about good human values and other life+soft skills. -->

  
## Publications

1. **Accelerating Computation of Steiner Trees on GPUs**
    - <u>Rajesh Pandian M</u>, Rupesh Nasre and N.S. Narayanaswamy.
    - International Journal of Parallel Programming **(IJPP)**, Vol 50, pgs 152–185 (2022). 
    - [(Preprint)]({static}/pdfs/steiner-ijpp22-preprint.pdf) [DOI][5] [Slides]({static}/pdfs/sem2-v4.pdf) [Video](https://youtu.be/BIecDhPdWaQ) [Code](https://doi.org/10.5281/zenodo.4477087) [BibTeX](https://dblp.org/rec/journals/ijpp/MuniasamyNN22.html?view=bibtex)
    <details> <summary>  Abstract </summary> 
      The Steiner Tree Problem (STP) is a well studied graph theoretic problem. It computes a minimum-weighted tree of a given graph such that the tree spans a given subset of vertices called terminals. STP is NP-hard. Due to its wide applicability, it has been a challenge problem in the 11th DIMACS implementation challenge and the PACE 2018 challenge. Due to its importance, polynomial-time approximation algorithms have been devised for solving the STP. One of the most popular algorithms is by Kou, Markowsky and Berman (KMB) which provides a 2-approximation to STP. In practice, a naïve implementation of the KMB algorithm is prohibitively slow for large graphs. Our goal in this work is to improve KMB algorithm’s practical utility by parallelizing it on GPU and reduce its execution time on real-world graphs. This parallelization faces several challenges due to the inherent irregular nature of computation, as well as critical design decisions affecting the algorithm choice and optimizations. We overcome these challenges with interesting algorithmic observations and by exploiting parallelization within sub-steps, and develop the first GPU-based efficient approach to computing Steiner trees using KMB. We illustrate the effectiveness of our approach using several graph benchmarks from the DIMACS Challenge, the PACE Challenge, SteinLib, and SNAP. Our highly optimized GPU implementation achieves an average 20× speedup over the CPU-sequential Open Graph algorithms and Data structure (OGDF)’s KMB implementation. In addition to this, our optimized CPU implementation achieves an average 4× over OGDF’s KMB, the only published open-source KMB implementation.
      </details>
    
2. **Effective Parallelization of the Vehicle Routing Problem.**
    - <u>Rajesh Pandian M </u>, Somesh Singh, Rupesh Nasre and N.S. Narayanaswamy.
    -  Proceedings of the Genetic and Evolutionary Computation Conference **(GECCO'23)**, pgs. 1036–1044 (2023).
    -  [DOI][6] [Slides]({static}/pdfs/gecco-cvrp-v3.pdf)  [Video](http://www.youtube.com/watch?v=IWgqRR-UO6U)   [Code](https://github.com/mrprajesh/parMDS) [BibTeX](https://dblp.org/rec/conf/gecco/Muniasamy0NN23.html?view=bibtex) <!--- [(Preprint)]({static}/pdfs/CVRP_v4.pdf) --->
     <details> <summary> Abstract </summary>
     Capacitated Vehicle Routing Problem (CVRP) is an important combinatorial optimization problem, which is also NP-hard. A wide array of heuristics have been proposed in the literature to obtain an approximate solution to CVRP. To improve the execution time, parallel methods have been developed for accelerating metaheuristics-based algorithms, genetic algorithms, and evolutionary algorithms for CVRP. Despite these advances, our experiments with the state-of-the-art parallel solutions indicate that their run times are too high to be practically useful. The combinatorial explosion is so high that the execution time is prohibitively large even on mid-sized CVRP instances having a few hundred customers. In this work, we propose a novel technique which combines local search and randomization for solving CVRP faster with reasonable accuracy, even on large problem instances. Our usage of randomization enables searching a large space of candidate solutions. We experimentally compare our proposed method with the state-of-the-art GPU implementations on diverse input instances and demonstrate the efficacy of our approach. Our sequential and shared-memory parallel implementations are on an average 36--1189× faster than the state-of-the-art GPU-parallel genetic algorithms while also achieving a superior solution quality. Furthermore, our reported solutions are close to the current best-known solutions from CVRPLIB. 
     </details>

3.  **StarPlat: A Versatile DSL for Graph Analytics.**
    - Nibedita Behera , Ashwina Kumar, Ebenezer Rajadurai T, Sai Nitish, <u>Rajesh Pandian M</u>, Rupesh Nasre.
    - **(Under review)** Journal of Parallel and Distributed Computing **(JPDC)**.  
    - [(arXiv PDF)](https://doi.org/10.48550/arXiv.2305.03317) [Code](https://github.com/nibeditabh/StarPlat)  [India Patented](https://drive.google.com/file/d/1BbzKyd0c8WGmbX1doh6gysPc3vuUlwU4/view?usp=sharing) // TODO [slides](#) [Video](#) Later after acceptance.  
    <details> <summary>  Abstract </summary>
     Graphs model several real-world phenomena. With the growth of unstructured and semi-structured data, parallelization of graph algorithms is inevitable. Unfortunately, due to inherent irregularity of computation, memory access, and communication, graph algorithms are traditionally challenging to parallelize. To tame this challenge, several libraries, frameworks, and domain-specific languages (DSLs) have been proposed to reduce the parallel programming burden of the users, who are often domain experts. However, existing frameworks to model graph algorithms typically target a single architecture. In this paper, we present a graph DSL, named StarPlat, that allows programmers to specify graph algorithms in a high-level format, but generates code for three different backends from the same algorithmic specification. In particular, the DSL compiler generates OpenMP for multi-core, MPI for distributed, and CUDA for many-core GPUs. Since these three are completely different parallel programming paradigms, binding them together under the same language is challenging. We share our experience with the language design. Central to our compiler is an intermediate representation which allows a common representation of the high-level program, from which individual backend code generations begin. We demonstrate the expressiveness of StarPlat by specifying four graph algorithms: betweenness centrality computation, page rank computation, single-source shortest paths, and triangle counting. We illustrate the effectiveness of our approach by comparing the performance of the generated codes with that obtained with hand-crafted library codes. We find that the generated code is competitive to library-based codes in many cases. More importantly, we show the feasibility to generate efficient codes for different target architectures from the same algorithmic specification of graph algorithms.
    </details>
    
4. **Code Generation for a Variety of Accelerators for a Graph DSL**
    - Ashwina Kumar, M. Venkata Krishna, Prasanna Bartakke, Rahul Kumar, <u>Rajesh Pandian M</u>, Nibedita Behera, Rupesh Nasre.
    - [(Manuscript/arXiv PDF)](https://doi.org/10.48550/arXiv.2401.02472) [Code](https://github.com/ashwinktpu/StarPlat)
    <details> <summary>  Abstract </summary>
     Sparse graphs are ubiquitous in real and virtual worlds. With the phenomenal growth in semi-structured and unstructured data, sizes of the underlying graphs have witnessed a rapid growth over the years. Analyzing such large structures necessitates parallel processing, which is challenged by the intrinsic irregularity of sparse computation, memory access, and communication. It would be ideal if programmers and domain-experts get to focus only on the sequential computation and a compiler takes care of auto-generating the parallel code. On the other side, there is a variety in the number of target hardware devices, and achieving optimal performance often demands coding in specific languages or frameworks. Our goal in this work is to focus on a graph DSL which allows the domain-experts to write almost-sequential code, and generate parallel code for different accelerators from the same algorithmic specification. In particular, we illustrate code generation from the StarPlat graph DSL for NVIDIA, AMD, and Intel GPUs using CUDA, OpenCL, SYCL, and OpenACC programming languages. Using a suite of ten large graphs and four popular algorithms, we present the efficacy of StarPlat's versatile code generator. 
    </details>

// More to follow.
    


## Patents

1. **Title:** System and method for automatic parallel code generation for graph algorithms for multiple target architectures, 
    - **Authors:** Rupesh Nasre, Ashwina Kumar, Ebenezer Rajadurai, Nibedita Behera, <u>Rajesh Pandian M</u>, Shan Mohammed, Sai Nitish, Jash Khatri, Naveen S, Shriram C, M Venkatakrishna and Rushabh Lalwani.                              
    - **India Patent Number**: 432922        
    - [(Certificate PDF)](https://drive.google.com/file/d/1BbzKyd0c8WGmbX1doh6gysPc3vuUlwU4/view?usp=sharing)

## Thesis
1. **Doctoral Thesis**
    - Title (Tentative): NP-hard Problems meet Parallelization.
<!--    - [PDF](#) [slides](#) [Video](#)  // TODO. Later  -->
2. **Master Thesis**
    - Fully Dynamic Maximal Matching in 3-Uniform Hypergraphs.
<!--- [slides](#)  // TODO   -->


Some of the problems we have/had worked on:

- Accelerating algorithms (approximate algorithms for NP-hard problems) using GPU. // PhD Thesis
- Designing exact algorithm for NP-hard problems (Treewidth, Minimum fill-in and Steiner tree). // Done in [PACE][2] 
- Solving Problems (such as Dominating set) on Grid.  // Visualisation Tool for Algorithmic solving. Done.
- Designing Dynamic Data Structures for Graph Problems // During Masters. Done.



[1]: http://www.cse.iitm.ac.in/~swamy/
[2]: https://pacechallenge.org
[3]: http://www.cse.iitm.ac.in/~rupesh/
[4]: https://rdcu.be/cCa9K
[5]: https://doi.org/10.1007/s10766-021-00723-0
[6]: https://doi.org/10.1145/3583131.3590458
[7]: https://dl.acm.org/doi/10.1145/3583131.3590458



> **(Disclaimer)** This material is presented to ensure timely dissemination of scholarly and technical work. Copyright and all rights therein are retained by authors or by other copyright holders. All persons copying this information are expected to adhere to the terms and constraints invoked by each author's copyright. In most cases, these works may not be reposted without the explicit permission of the copyright holder.
