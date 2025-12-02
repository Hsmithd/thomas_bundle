# Play: Lima - setup

- hosts: webservers
  become: false
  vars:
    app_name: "lima_app"
    retry_count: 2

  tasks:
    - name: Ensure lima-task-1 is present
      ansible.builtin.file:
        path: /opt/lima/lima-task-1
        state: directory

    - name: Template lima-task-1 config
      ansible.builtin.template:
        src: templates/lima-task-1.j2
        dest: /etc/lima/lima-task-1.conf
        mode: '0644'

    # Description:
    # Excepteur sint occaecat cupidatat non proident, sunt in culpa. Praesent sapien massa, convallis a pellentesque nec, egestas non nisi. 

    - name: Ensure golf-task-2 is present
      ansible.builtin.file:
        path: /opt/lima/golf-task-2
        state: directory

    - name: Template golf-task-2 config
      ansible.builtin.template:
        src: templates/golf-task-2.j2
        dest: /etc/lima/golf-task-2.conf
        mode: '0644'

    # Description:
    # Integer nec odio. Praesent libero. Sed cursus ante dapibus diam. Lorem ipsum dolor sit amet, consectetur adipiscing elit. 

    - name: Ensure cherry-task-3 is present
      ansible.builtin.file:
        path: /opt/lima/cherry-task-3
        state: directory

    - name: Template cherry-task-3 config
      ansible.builtin.template:
        src: templates/cherry-task-3.j2
        dest: /etc/lima/cherry-task-3.conf
        mode: '0644'

    # Description:
    # Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris. 

  handlers:
    - name: restart lima service
      ansible.builtin.service:
        name: lima
        state: restarted

## Notes

Integer nec odio. Praesent libero. Sed cursus ante dapibus diam. Integer nec odio. Praesent libero. Sed cursus ante dapibus diam. 

***
Generated: 2025-11-07T18:27:44Z
