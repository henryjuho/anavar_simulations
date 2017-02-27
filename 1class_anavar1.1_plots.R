library(ggplot2)

args <- commandArgs(TRUE)
input_file = args[1]

test_data = subset(read.delim(input_file), sim_e_1 != 0)

f <- function(x) {
  r <- quantile(x, probs = c(0.025, 0.25, 0.5, 0.75, 0.975))
  names(r) <- c("ymin", "lower", "middle", "upper", "ymax")
  r
}

theta <- ggplot(test_data, aes(x=sim_theta_1, y=data_1_theta_1)) + 
  stat_summary(fun.data = f, geom="boxplot") +
  theme_bw(base_size = 10) +
  facet_wrap(~sim_e_1, ncol = 3) +
  labs(x=expression(theta[simulated]), y=expression(theta[predicted])) +
  #ylim(0,1750) +
  xlim(0,max(as.numeric(test_data$data_1_theta_1), na.rm=TRUE)) +
  theme(axis.title = element_text(size = 20, face = 'bold'), 
        axis.text = element_text(size = 15, face = 'bold'),
        strip.text.x = element_text(size = 13, face = 'bold'))

ggsave('1class.1snps.anavar1.1.theta.jpg', theta, width=15, height=7)

gamma <- ggplot(test_data, aes(x=sim_gamma_1, y=data_1_gamma_1)) + 
  stat_summary(fun.data = f, geom="boxplot") +
  theme_bw(base_size = 10) +
  facet_wrap(~sim_e_1, ncol = 3) +
  labs(x=expression(gamma[simulated]), y=expression(gamma[predicted])) +
  #ylim(0,1750) +
  #xlim(0,max(as.numeric(test_data$data_1_gamma_1), na.rm=TRUE)) +
  theme(axis.title = element_text(size = 20, face = 'bold'), 
        axis.text = element_text(size = 15, face = 'bold'),
        strip.text.x = element_text(size = 13, face = 'bold'))

ggsave('1class.1snps.anavar1.1.gamma.jpg', gamma, width=15, height=7)

error <- ggplot(test_data, aes(x=sim_e_1, y=data_1_e_1)) + 
  stat_summary(fun.data = f, geom="boxplot") +
  theme_bw(base_size = 10) +
  #facet_wrap(~sim_e_1, ncol = 3) +
  labs(x=expression(e[simulated]), y=expression(e[predicted])) +
  #ylim(0,1750) +
  theme(axis.title = element_text(size = 20, face = 'bold'), 
        axis.text = element_text(size = 15, face = 'bold'),
        strip.text.x = element_text(size = 13, face = 'bold'))

ggsave('1class.1snps.anavar1.1.error.jpg', error, width=7, height=7)
