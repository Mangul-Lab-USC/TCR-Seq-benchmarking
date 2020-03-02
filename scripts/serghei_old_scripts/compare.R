#! /usr/bin/env Rscript

 

# test if there is at least one argument: if not, return an error
if (length(args)<1) {
    print ("1: prefix")
    stop("At least 1 argument must be supplied : prefix", call.=FALSE)
}

args <- commandArgs(trailingOnly = TRUE)

library(ggplot2)
library("ggpubr")

#Correlation plot
file_FREQ_both_csv<-paste(args[1],".correlation.common.FREQ.both.csv",sep="")
file_FREQ_both_pdf<-paste(args[1],".correlation.common.FREQ.both.png",sep="")

data=read.csv(file_FREQ_both_csv)



png(file_FREQ_both_pdf)
ggscatter(data, x = "FREQ.ImReP", y = "FREQ.TCR.Seq", add = "reg.line", conf.int = TRUE, cor.coef = TRUE, cor.method = "pearson",xlab = "RNA-Seq", ylab = "TCR-SEQ")
dev.off()

#==========================================
# FREQ of clonotypes from TCR-Seq colored based if it also confirmed by ImreP


file_FREQ_only_TCRSEQ_csv<-paste(args[1],".FREQ.TCR.Seq.csv",sep="")


###1
file_FREQ_only_TCRSEQ_pdf1<-paste(args[1],".FREQ.TCR.Seq.png",sep="")

data=read.csv(file_FREQ_only_TCRSEQ_csv)


png(file_FREQ_only_TCRSEQ_pdf1)
ggplot(data) + geom_point(aes(n,FREQ.TCR.Seq,color=common.flag))
dev.off()

####2
file_FREQ_only_TCRSEQ_pdf2<-paste(args[1],".FREQ.TCR.Seq.zoom.png",sep="")
data=read.csv(file_FREQ_only_TCRSEQ_csv)


png(file_FREQ_only_TCRSEQ_pdf2)
ggplot(data) + geom_point(aes(n,FREQ.TCR.Seq,color=common.flag))+scale_y_continuous(limits = c(0, 0.01))
dev.off()


#==========================================
# FREQ of clonotypes from ImreP colored based if it also confirmed by TCR-Seq

file_FREQ_imrep_csv<-paste(args[1],".RNASEQ.FREQ.csv",sep="")


###1
file_FREQ_imrep_pdf1<-paste(args[1],".RNASEQ.FREQ.png",sep="")

data=read.csv(file_FREQ_imrep_csv)


png(file_FREQ_imrep_pdf1)
ggplot(data) + geom_point(aes(n,count,color=common.flag))
dev.off()

####2
file_FREQ_imrep_pdf2<-paste(args[1],".RNASEQ.FREQ.zoom.png",sep="")
data=read.csv(file_FREQ_imrep_csv)


png(file_FREQ_imrep_pdf2)
ggplot(data) + geom_point(aes(n,count,color=common.flag))+scale_y_continuous(limits = c(0, 100))
dev.off()